import 'dart:convert';
import 'package:flutter/services.dart';
import 'package:flutter/material.dart';
import '../models/question.dart';
import '../models/module.dart';

class FlashcardsScreen extends StatefulWidget {
  const FlashcardsScreen({super.key});
  @override
  State<FlashcardsScreen> createState() => _FlashcardsScreenState();
}

class _FlashcardsScreenState extends State<FlashcardsScreen> {
  List<Question> all = [];
  int idx = 0;
  bool showAns = false;
  bool loading = true;
  final int limit = 50;

  @override
  void initState() { super.initState(); load(); }

  Future<void> load() async {
    List<String> files = [
      'assets/questions/life_questions.json',
      'assets/questions/ethics_questions.json',
      'assets/questions/accident_sickness_questions.json',
      'assets/questions/disability_questions.json',
      'assets/questions/critical_illness_questions.json',
      'assets/questions/segregated_funds_questions.json',
      'assets/questions/annuities_questions.json',
      'assets/questions/estate_questions.json',
      'assets/questions/taxation_questions.json',
    ];
    List<Question> temp = [];
    for (var f in files) {
      try {
        String data = await rootBundle.loadString(f);
        List<dynamic> j = json.decode(data);
        temp.addAll(j.map((e) => Question.fromJson(e)));
      } catch (e) {}
    }
    temp.shuffle();
    setState(() { all = temp.take(limit).toList(); loading = false; idx = 0; });
  }

  void _prev() { if (idx > 0) setState(() { idx--; showAns = false; }); }
  void _next() { if (idx < all.length - 1) setState(() { idx++; showAns = false; }); }

  @override
  Widget build(BuildContext context) {
    if (loading) return Scaffold(appBar: AppBar(title: const Text("Flashcards")), body: const Center(child: CircularProgressIndicator()));
    if (all.isEmpty) return Scaffold(appBar: AppBar(title: const Text("Flashcards")), body: const Center(child: Text("No questions")));
    var q = all[idx];
    return Scaffold(
      backgroundColor: const Color(0xFFF5F7FB),
      appBar: AppBar(title: Text("Flashcards ${idx + 1}/${all.length}"), centerTitle: true, backgroundColor: Colors.white, elevation: 0),
      body: Column(
        children: [
          ClipRRect(borderRadius: BorderRadius.circular(10), child: LinearProgressIndicator(value: (idx + 1) / all.length, minHeight: 6, backgroundColor: Colors.grey[200])),
          Padding(
            padding: const EdgeInsets.all(12),
            child: Container(padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6), decoration: BoxDecoration(color: Colors.indigo, borderRadius: BorderRadius.circular(20)), child: Text("${idx + 1} / ${all.length}", style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold))),
          ),
          Expanded(
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Card(
                elevation: 8,
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
                child: Padding(
                  padding: const EdgeInsets.all(24),
                  child: SingleChildScrollView(
                    child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text("Q${idx + 1}: ${q.question}", style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, height: 1.4)),
                      const SizedBox(height: 20),
                      if (showAns)...[
                        const Divider(),
                        const SizedBox(height: 12),
                        Container(padding: const EdgeInsets.all(12), decoration: BoxDecoration(color: Colors.green[50], borderRadius: BorderRadius.circular(12)), child: Text("Answer: ${q.options[q.correctAnswer]}", style: TextStyle(fontSize: 16, color: Colors.green[800], fontWeight: FontWeight.bold))),
                        const SizedBox(height: 16),
                        Text(q.explanation, style: const TextStyle(fontSize: 14, height: 1.5)),
                      ],
                    ]),
                  ),
                ),
              ),
            ),
          ),
          Padding(padding: const EdgeInsets.symmetric(horizontal: 16), child: SizedBox(width: double.infinity, child: ElevatedButton(onPressed: () => setState(() => showAns =!showAns), child: Text(showAns? "Hide Answer" : "Show Answer")))),
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 12, 16, 24),
            child: Row(mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [
              ElevatedButton(onPressed: idx > 0? _prev : null, child: const Text("Previous")),
              Text("${idx + 1}/${all.length}", style: const TextStyle(fontWeight: FontWeight.bold)),
              ElevatedButton(onPressed: idx < all.length - 1? _next : null, child: Text(idx == all.length - 1? "Done" : "Next")),
            ]),
          ),
        ],
      ),
    );
  }
}
