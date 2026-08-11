import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/module.dart';
import '../providers/quiz_provider.dart';
import 'result_screen.dart';

class QuizScreen extends StatefulWidget {
  final ModuleInfo module;
  const QuizScreen({super.key, required this.module});

  @override
  State<QuizScreen> createState() => _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen> {
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      Provider.of<QuizProvider>(context, listen: false).loadModule(widget.module);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Consumer<QuizProvider>(
      builder: (context, provider, _) {
        if (provider.isLoading) {
          return Scaffold(appBar: AppBar(title: Text(widget.module.name)), body: const Center(child: CircularProgressIndicator()));
        }
        if (provider.questions.isEmpty) {
          return Scaffold(
            appBar: AppBar(title: Text(widget.module.name)),
            body: Center(child: Text('No questions found in ${widget.module.assetFile}')),
          );
        }
        final q = provider.currentQuestion;
        return Scaffold(
          appBar: AppBar(
            title: Text('${widget.module.name} ${provider.currentIndex+1}/${provider.totalQuestions} - Score ${provider.score}'),
            bottom: PreferredSize(preferredSize: const Size.fromHeight(6), child: LinearProgressIndicator(value: provider.progress)),
          ),
          body: SingleChildScrollView(
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(children: [
                  Chip(label: Text(q.topic)),
                  const SizedBox(width: 8),
                  Chip(label: Text(q.difficulty), backgroundColor: q.difficulty=='Easy'? Colors.green[100]: q.difficulty=='Medium'? Colors.orange[100]: Colors.red[100]),
                ]),
                const SizedBox(height: 12),
                Text('Q${provider.currentIndex+1}: ${q.question}', style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w600)),
                const SizedBox(height: 20),
                ...List.generate(q.options.length, (i) {
                  final isCorrect = i == q.correctAnswer;
                  final isSelected = i == provider.selectedAnswer;
                  Color? bg;
                  IconData? icon;
                  if (provider.showExplanation) {
                    if (isCorrect) { bg = Colors.green.shade100; icon = Icons.check_circle; }
                    else if (isSelected) { bg = Colors.red.shade100; icon = Icons.cancel; }
                  } else if (isSelected) {
                    bg = Colors.blue.shade50;
                  }
                  return Card(
                    color: bg,
                    child: ListTile(
                      title: Text(q.options[i]),
                      leading: CircleAvatar(backgroundColor: isSelected? Colors.indigo: null, child: Text(String.fromCharCode(65+i), style: TextStyle(color: isSelected? Colors.white: null))),
                      onTap: () => provider.selectAnswer(i),
                      trailing: icon!=null? Icon(icon, color: isCorrect? Colors.green: Colors.red) : null,
                    ),
                  );
                }),
                if (provider.showExplanation)...[
                  const SizedBox(height: 16),
                  Container(
                    width: double.infinity,
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(color: Colors.indigo.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.indigo.shade100)),
                    child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      const Text('Explanation:', style: TextStyle(fontWeight: FontWeight.bold)),
                      const SizedBox(height: 6),
                      Text(q.explanation, style: const TextStyle(fontSize: 14, height: 1.4)),
                    ]),
                  ),
                  const SizedBox(height: 80),
                ] else ...[
                  const SizedBox(height: 16),
                  const Text('👆 Select an answer to continue', style: TextStyle(color: Colors.grey)),
                ],
              ],
            ),
          ),
          bottomNavigationBar: SafeArea(
            child: Padding(
              padding: const EdgeInsets.all(12),
              child: Row(
                children: [
                  if (provider.currentIndex > 0) Expanded(child: OutlinedButton.icon(icon: const Icon(Icons.arrow_back), onPressed: provider.previousQuestion, label: const Text('Prev'))),
                  if (provider.currentIndex > 0) const SizedBox(width: 12),
                  Expanded(
                    flex: 2,
                    child: ElevatedButton.icon(
                      icon: Icon(provider.isLastQuestion? Icons.flag : Icons.arrow_forward),
                      style: ElevatedButton.styleFrom(
                        backgroundColor: provider.showExplanation? Colors.indigo: Colors.grey,
                        foregroundColor: Colors.white,
                        padding: const EdgeInsets.symmetric(vertical: 14),
                      ),
                      onPressed: provider.showExplanation? () {
                        if (provider.isLastQuestion) {
                          Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => ResultScreen(provider: provider)));
                        } else {
                          provider.nextQuestion();
                        }
                      } : null,
                      label: Text(provider.isLastQuestion? 'Result (${provider.currentIndex+1}/${provider.totalQuestions})' : 'Next (${provider.currentIndex+1}/${provider.totalQuestions})'),
                    ),
                  ),
                ],
              ),
            ),
          ),
        );
      },
    );
  }
}
