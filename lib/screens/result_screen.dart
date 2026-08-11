import 'package:flutter/material.dart';
import '../providers/quiz_provider.dart';

class ResultScreen extends StatelessWidget {
  final QuizProvider provider;
  const ResultScreen({super.key, required this.provider});

  @override
  Widget build(BuildContext context) {
    final percent = provider.totalQuestions == 0? 0 : (provider.score / provider.totalQuestions * 100).toInt();
    final passed = percent >= 60;
    return Scaffold(
      appBar: AppBar(title: const Text('Result')),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(passed? Icons.celebration : Icons.sentiment_dissatisfied, size: 80, color: passed? Colors.green : Colors.red),
              const SizedBox(height: 16),
              Text('${provider.score} / ${provider.totalQuestions}', style: const TextStyle(fontSize: 32, fontWeight: FontWeight.bold)),
              Text('$percent%', style: TextStyle(fontSize: 24, color: passed? Colors.green : Colors.red)),
              Text(passed? 'PASSED' : 'NEEDS PRACTICE', style: const TextStyle(fontSize: 18)),
              const SizedBox(height: 24),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  ElevatedButton(onPressed: () { provider.reset(); Navigator.pop(context); }, child: const Text('Retry')),
                  const SizedBox(width: 12),
                  OutlinedButton(onPressed: () => Navigator.popUntil(context, (r) => r.isFirst), child: const Text('Home')),
                ],
              )
            ],
          ),
        ),
      ),
    );
  }
}
