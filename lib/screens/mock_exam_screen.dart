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
  String? loadError;
  List<Question> allQs = [];

  @override
  void initState() {
    super.initState();
    loadAll();
  }

  Future<List<Question>> _loadBank(String assetPath) async {
    final data = await rootBundle.loadString(assetPath);
    final List<dynamic> decoded = json.decode(data);
    return decoded.map((e) => Question.fromJson(e as Map<String, dynamic>)).toList();
  }

  List<Question> _pick(List<Question> source, int count) {
    final copy = List<Question>.from(source)..shuffle();
    if (copy.length <= count) return copy;
    return copy.take(count).toList();
  }

  Future<void> loadAll() async {
    setState(() {
      loading = true;
      loadError = null;
    });

    try {
      // The harmonized LLQP is examined in four separate modules:
      // Life Insurance, Accident & Sickness, Segregated Funds & Annuities,
      // and Ethics & Professional Practice. This app uses nine study sections,
      // so the 100-question comprehensive practice mock maps those sections
      // into the four official exam areas and gives each area 25 questions.
      final life = await _loadBank('assets/questions/life_questions.json');
      final estate = await _loadBank('assets/questions/estate_questions.json');
      final taxation = await _loadBank('assets/questions/taxation_questions.json');

      final accidentSickness =
          await _loadBank('assets/questions/accident_sickness_questions.json');
      final disability =
          await _loadBank('assets/questions/disability_questions.json');
      final criticalIllness =
          await _loadBank('assets/questions/critical_illness_questions.json');

      final segFunds =
          await _loadBank('assets/questions/seg_funds_questions.json');
      final annuities =
          await _loadBank('assets/questions/annuities_questions.json');

      final ethics = await _loadBank('assets/questions/ethics_questions.json');

      final selected = <Question>[
        // Life Insurance area: 25
        ..._pick(life, 15),
        ..._pick(estate, 5),
        ..._pick(taxation, 5),

        // Accident & Sickness area: 25
        ..._pick(accidentSickness, 11),
        ..._pick(disability, 8),
        ..._pick(criticalIllness, 6),

        // Segregated Funds & Annuities area: 25
        ..._pick(segFunds, 13),
        ..._pick(annuities, 12),

        // Ethics & Professional Practice area: 25
        ..._pick(ethics, 25),
      ]..shuffle();

      if (!mounted) return;
      setState(() {
        allQs = selected;
        loading = false;
      });
    } catch (e) {
      debugPrint('Failed to build mock exam: $e');
      if (!mounted) return;
      setState(() {
        loading = false;
        loadError = 'Unable to load the complete mock exam. Please try again.';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    if (loading) {
      return Scaffold(
        appBar: AppBar(title: const Text('Mock Exam')),
        body: const Center(child: CircularProgressIndicator()),
      );
    }

    if (loadError != null) {
      return Scaffold(
        appBar: AppBar(title: const Text('Mock Exam')),
        body: Center(
          child: Padding(
            padding: const EdgeInsets.all(24),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(loadError!, textAlign: TextAlign.center),
                const SizedBox(height: 16),
                ElevatedButton(
                  onPressed: loadAll,
                  child: const Text('Try Again'),
                ),
              ],
            ),
          ),
        ),
      );
    }

    final mockModule = ModuleInfo(
      id: 'mock',
      name: 'Comprehensive LLQP Mock',
      assetFile: 'assets/questions/life_questions.json',
      icon: '📝',
      color: '#000000',
      description: '100-question practice exam across the four LLQP exam areas',
    );

    return Scaffold(
      appBar: AppBar(title: Text('Mock Exam - ${allQs.length} Qs')),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Text(
                'Comprehensive LLQP Practice Mock',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 12),
              const Text(
                '100 questions: 25 each from Life Insurance, Accident & Sickness, Segregated Funds & Annuities, and Ethics & Professional Practice.',
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 10),
              const Text(
                'This is a comprehensive study mock. The actual harmonized LLQP licensing examination is administered as separate modules.',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 13),
              ),
              const SizedBox(height: 30),
              ElevatedButton(
                onPressed: allQs.length == 100
                    ? () {
                        final provider =
                            Provider.of<QuizProvider>(context, listen: false);
                        provider.setCustomQuestions(allQs, mockModule);
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (_) => QuizScreen(module: mockModule),
                          ),
                        );
                      }
                    : null,
                child: const Text('Start Mock Exam'),
              ),
              const SizedBox(height: 12),
              TextButton(
                onPressed: loadAll,
                child: const Text('Generate New Mock'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
