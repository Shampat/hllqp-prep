class Question {
  final dynamic id; // allow int or String
  final String moduleId;
  final String moduleName;
  final String topic;
  final String difficulty;
  final String question;
  final List<String> options;
  final int correctAnswer;
  final String explanation;

  Question({
    required this.id,
    required this.moduleId,
    required this.moduleName,
    required this.topic,
    required this.difficulty,
    required this.question,
    required this.options,
    required this.correctAnswer,
    required this.explanation,
  });

  factory Question.fromJson(Map<String, dynamic> json) {
    final dynamic parsedId = json['id'] ?? 0;
    final rawOptions = json['options'] != null
        ? List<String>.from(json['options'].map((e) => e.toString()))
        : <String>["A", "B", "C", "D"];
    final rawCorrectAnswer = json['correctAnswer'] is int
        ? json['correctAnswer'] as int
        : int.tryParse(json['correctAnswer'].toString()) ?? 0;

    // Rotate option positions deterministically so a bank that happens to store
    // many correct answers in the same JSON slot does not teach users an
    // answer-position pattern. Using the question id keeps option order stable
    // across app restarts, which is important when progress is resumed.
    final optionCount = rawOptions.length;
    int shift = 0;
    if (optionCount > 0) {
      final numericId = parsedId is int
          ? parsedId
          : int.tryParse(parsedId.toString());
      if (numericId != null) {
        shift = numericId % optionCount;
      } else {
        shift = parsedId.toString().codeUnits.fold<int>(0, (a, b) => a + b) % optionCount;
      }
    }

    final rotatedOptions = optionCount == 0
        ? <String>[]
        : <String>[
            ...rawOptions.skip(shift),
            ...rawOptions.take(shift),
          ];
    final rotatedCorrectAnswer = optionCount == 0
        ? 0
        : (rawCorrectAnswer - shift) % optionCount;

    return Question(
      id: parsedId,
      moduleId: json['moduleId']?.toString() ?? json['module']?.toString() ?? 'life',
      moduleName: json['moduleName']?.toString() ?? json['moduleId']?.toString() ?? 'Life',
      topic: json['topic']?.toString() ?? 'General',
      difficulty: json['difficulty']?.toString() ?? 'Medium',
      question: json['question']?.toString() ?? '',
      options: rotatedOptions,
      correctAnswer: rotatedCorrectAnswer,
      explanation: json['explanation']?.toString() ?? 'No explanation',
    );
  }
}