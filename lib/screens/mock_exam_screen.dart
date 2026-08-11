import 'dart:convert';
import 'package:flutter/services.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/quiz_provider.dart';
import '../models/question.dart';
import '../models/module.dart';
import 'quiz_screen.dart';

class MockExamScreen extends StatefulWidget {
  const MockExamScreen({super.key});
  @override
  State<MockExamScreen> createState() => _MockExamScreenState();
}

class _MockExamScreenState extends State<MockExamScreen> {
  bool loading = true;
  List<Question> allQs = [];

  @override
  void initState() {
    super.initState();
    loadAll();
  }

  Future<void> loadAll() async {
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
      } catch (e) {
        debugPrint("Failed $f $e");
      }
    }
    temp.shuffle();
    allQs = temp.take(temp.length < 100? temp.length : 100).toList();
    setState(() => loading = false);
  }

  @override
  Widget build(BuildContext context) {
    if (loading) return Scaffold(appBar: AppBar(title: Text("Mock Exam")), body: Center(child: CircularProgressIndicator()));
    var mockModule = ModuleInfo(id: 'mock', name: 'Mock Exam (${allQs.length} Q)', assetFile: 'assets/questions/life_questions.json', icon: '📝', color: '#000000', description: 'Provincial style mock');
    return Scaffold(
      appBar: AppBar(title: Text("Mock Exam - ${allQs.length} Qs")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text("Provincial Style Mock", style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            SizedBox(height: 10),
            Text("${allQs.length} questions mixed from all modules"),
            SizedBox(height: 30),
            ElevatedButton(
              onPressed: () {
                final provider = Provider.of<QuizProvider>(context, listen: false);
                provider.setCustomQuestions(allQs, mockModule);
                Navigator.push(context, MaterialPageRoute(builder: (_) => QuizScreen(module: mockModule)));
              },
              child: Text("Start Mock Exam"),
            )
          ],
        ),
      ),
    );
  }
}
