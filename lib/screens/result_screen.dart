import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/module.dart';
import '../providers/quiz_provider.dart';
import '../services/premium_service.dart';
import 'paywall_screen.dart';

class ResultScreen extends StatelessWidget {
  final QuizProvider provider;
  const ResultScreen({super.key, required this.provider});

  @override
  Widget build(BuildContext context) {
    final percent = provider.totalQuestions == 0 ? 0 : (provider.score / provider.totalQuestions * 100).toInt();
    final passed = percent >= 60;
    final premium = context.watch<PremiumService>();
    final moduleIndex = allModules.indexWhere((m) => m.id == provider.currentModule?.id);
    final isFreePreview = !premium.isPro &&
        moduleIndex >= PremiumService.fullyFreeModuleCount &&
        provider.totalQuestions == PremiumService.freePreviewQuestionCount;

    return Scaffold(
      appBar: AppBar(title: const Text('Result')),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(passed ? Icons.celebration : Icons.sentiment_dissatisfied, size: 80, color: passed ? Colors.green : Colors.red),
              const SizedBox(height: 16),
              Text('${provider.score} / ${provider.totalQuestions}', style: const TextStyle(fontSize: 32, fontWeight: FontWeight.bold)),
              Text('$percent%', style: TextStyle(fontSize: 24, color: passed ? Colors.green : Colors.red)),
              Text(passed ? 'PASSED' : 'NEEDS PRACTICE', style: const TextStyle(fontSize: 18)),
              if (isFreePreview) ...[
                const SizedBox(height: 24),
                const Text(
                  'You completed the 10-question free preview. Unlock Pro for all 60 questions in this module, all 540 questions, full flashcards, comprehensive mocks, and no banner ads.',
                  textAlign: TextAlign.center,
                ),
                const SizedBox(height: 12),
                ElevatedButton.icon(
                  onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const PaywallScreen())),
                  icon: const Icon(Icons.lock_open),
                  label: const Text('Unlock All with Pro'),
                ),
              ],
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
