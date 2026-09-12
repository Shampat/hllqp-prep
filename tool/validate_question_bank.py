#!/usr/bin/env python3
"""Validate the nine active HLLQP study-section question banks.

Checks structural integrity, ids, module ids, exact duplicate stems, option quality,
answer indexes, explanations, difficulty values, and answer-position distribution.
The app rotates answer options deterministically by question id, so this validator
reports both raw JSON positions and effective runtime positions.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTIONS_DIR = ROOT / "assets" / "questions"

ACTIVE = {
    "life_questions.json": "life",
    "accident_sickness_questions.json": "accident_sickness",
    "disability_questions.json": "disability",
    "critical_illness_questions.json": "critical_illness",
    "seg_funds_questions.json": "seg_funds",
    "annuities_questions.json": "annuities",
    "estate_questions.json": "estate",
    "taxation_questions.json": "taxation",
    "ethics_questions.json": "ethics",
}

REQUIRED_FIELDS = {
    "id",
    "moduleId",
    "question",
    "options",
    "correctAnswer",
    "explanation",
    "topic",
    "difficulty",
}

VALID_DIFFICULTIES = {"Easy", "Medium", "Hard"}
SUSPICIOUS_PADDING = re.compile(
    r"\bregarding\s+(taxation|eligibility|calculation|application)\b",
    re.IGNORECASE,
)


def normalize(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def runtime_correct_index(question_id: object, correct: int, option_count: int) -> int:
    if option_count <= 0:
        return 0
    try:
        numeric_id = int(question_id)
        shift = numeric_id % option_count
    except (TypeError, ValueError):
        shift = sum(ord(ch) for ch in str(question_id)) % option_count
    return (correct - shift) % option_count


def fail(errors: list[str], where: str, message: str) -> None:
    errors.append(f"{where}: {message}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    all_questions: list[tuple[str, dict]] = []
    normalized_stems: dict[str, list[tuple[str, object]]] = defaultdict(list)

    print("HLLQP question-bank validation")
    print("=" * 32)

    for filename, expected_module in ACTIVE.items():
        path = QUESTIONS_DIR / filename
        if not path.exists():
            fail(errors, filename, "file is missing")
            continue

        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 - validator should report any parse failure
            fail(errors, filename, f"invalid JSON: {exc}")
            continue

        if not isinstance(data, list):
            fail(errors, filename, "top-level JSON must be an array")
            continue

        if len(data) != 60:
            fail(errors, filename, f"expected 60 questions, found {len(data)}")

        ids: list[object] = []
        raw_positions: Counter[int] = Counter()
        runtime_positions: Counter[int] = Counter()
        difficulties: Counter[str] = Counter()

        for index, q in enumerate(data, start=1):
            where = f"{filename} question #{index}"
            if not isinstance(q, dict):
                fail(errors, where, "record must be an object")
                continue

            missing = REQUIRED_FIELDS - set(q)
            if missing:
                fail(errors, where, f"missing fields: {sorted(missing)}")
                continue

            qid = q["id"]
            ids.append(qid)

            if q["moduleId"] != expected_module:
                fail(
                    errors,
                    where,
                    f"moduleId {q['moduleId']!r} does not match {expected_module!r}",
                )

            question = q["question"]
            if not isinstance(question, str) or not question.strip():
                fail(errors, where, "question stem must be a non-empty string")
            else:
                stem = normalize(question)
                normalized_stems[stem].append((filename, qid))
                if SUSPICIOUS_PADDING.search(question):
                    warnings.append(f"{where}: suspicious legacy padding phrase")

            options = q["options"]
            if not isinstance(options, list) or len(options) != 4:
                fail(errors, where, "options must contain exactly 4 choices")
                option_count = len(options) if isinstance(options, list) else 0
            else:
                option_count = 4
                if any(not isinstance(opt, str) or not opt.strip() for opt in options):
                    fail(errors, where, "all options must be non-empty strings")
                normalized_options = [normalize(str(opt)) for opt in options]
                if len(set(normalized_options)) != 4:
                    fail(errors, where, "options must be distinct")

            correct = q["correctAnswer"]
            if not isinstance(correct, int) or not 0 <= correct <= 3:
                fail(errors, where, "correctAnswer must be an integer from 0 to 3")
            else:
                raw_positions[correct] += 1
                runtime_positions[
                    runtime_correct_index(qid, correct, option_count)
                ] += 1

            explanation = q["explanation"]
            if not isinstance(explanation, str) or len(explanation.strip()) < 20:
                fail(errors, where, "explanation is missing or too short")

            topic = q["topic"]
            if not isinstance(topic, str) or not topic.strip():
                fail(errors, where, "topic must be a non-empty string")

            difficulty = q["difficulty"]
            if difficulty not in VALID_DIFFICULTIES:
                fail(
                    errors,
                    where,
                    f"difficulty must be one of {sorted(VALID_DIFFICULTIES)}",
                )
            else:
                difficulties[difficulty] += 1

            all_questions.append((filename, q))

        if len(set(map(str, ids))) != len(ids):
            fail(errors, filename, "question ids are not unique")

        # Rewritten banks intentionally use ids 1..60.
        numeric_ids = []
        for qid in ids:
            try:
                numeric_ids.append(int(qid))
            except (TypeError, ValueError):
                numeric_ids = []
                break
        if numeric_ids and sorted(numeric_ids) != list(range(1, 61)):
            fail(errors, filename, "numeric ids must be exactly 1 through 60")

        if data:
            if raw_positions and max(raw_positions.values()) > 30:
                warnings.append(
                    f"{filename}: raw JSON answer positions are biased {dict(sorted(raw_positions.items()))}; "
                    "runtime option rotation mitigates this"
                )
            if runtime_positions and max(runtime_positions.values()) - min(
                runtime_positions.get(i, 0) for i in range(4)
            ) > 15:
                fail(
                    errors,
                    filename,
                    f"effective runtime answer positions remain too imbalanced: "
                    f"{dict(sorted(runtime_positions.items()))}",
                )
            if len(difficulties) < 3:
                warnings.append(
                    f"{filename}: not all three difficulty levels are represented: {dict(difficulties)}"
                )

        print(
            f"{filename:38} count={len(data):2} "
            f"raw={dict(sorted(raw_positions.items()))} "
            f"runtime={dict(sorted(runtime_positions.items()))} "
            f"difficulty={dict(difficulties)}"
        )

    # Exact duplicate stems anywhere in the active 540-question bank are errors.
    for stem, occurrences in normalized_stems.items():
        if stem and len(occurrences) > 1:
            locations = ", ".join(f"{f}#{qid}" for f, qid in occurrences)
            fail(errors, "cross-bank", f"exact duplicate stem at {locations}")

    # Near-duplicate detection is a warning because related modules can legitimately
    # assess the same concept from different angles.
    by_file: dict[str, list[dict]] = defaultdict(list)
    for filename, q in all_questions:
        by_file[filename].append(q)

    for filename, questions in by_file.items():
        for i in range(len(questions)):
            a = normalize(str(questions[i].get("question", "")))
            if len(a) < 35:
                continue
            for j in range(i + 1, len(questions)):
                b = normalize(str(questions[j].get("question", "")))
                if len(b) < 35:
                    continue
                ratio = SequenceMatcher(None, a, b).ratio()
                if ratio >= 0.92:
                    warnings.append(
                        f"{filename}: possible near-duplicate ids "
                        f"{questions[i].get('id')} and {questions[j].get('id')} ({ratio:.2f})"
                    )

    print()
    print(f"Active records checked: {len(all_questions)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"  - {warning}")

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("\nPASS: all active question banks satisfy structural validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
