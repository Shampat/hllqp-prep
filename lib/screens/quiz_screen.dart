import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/module.dart';
import '../providers/quiz_provider.dart';
import '../providers/theme_provider.dart';
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
    final isDark = Provider.of<ThemeProvider>(context).isDark;
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
            title: Text('${widget.module.name} ${provider.currentIndex+1}/${provider.totalQuestions} - Score ${provider.score}', style: const TextStyle(fontSize: 13), overflow: TextOverflow.ellipsis),
            bottom: PreferredSize(preferredSize: const Size.fromHeight(6), child: LinearProgressIndicator(value: provider.progress, backgroundColor: isDark? Colors.white24 : Colors.black12)),
          ),
          body: SingleChildScrollView(
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(children: [
                  Chip(label: Text(q.topic, style: TextStyle(fontSize: 11, color: isDark? Colors.white : Colors.black87)), backgroundColor: isDark? const Color(0xFF2A2A2A) : Colors.grey[200]),
                  const SizedBox(width: 8),
                  Chip(label: Text(q.difficulty, style: const TextStyle(fontSize: 11)), backgroundColor: q.difficulty=='Easy'? (isDark? Colors.green[900] : Colors.green[100]) : q.difficulty=='Medium'? (isDark? Colors.orange[900] : Colors.orange[100]) : (isDark? Colors.red[900] : Colors.red[100])),
                ]),
                const SizedBox(height: 12),
                Text('Q${provider.currentIndex+1}: ${q.question}', style: TextStyle(fontSize: 18, fontWeight: FontWeight.w700, height: 1.4, color: isDark? Colors.white : Colors.black87)),
                const SizedBox(height: 20),
                ...List.generate(q.options.length, (i) {
                  final isCorrect = i == q.correctAnswer;
                  final isSelected = i == provider.selectedAnswer;
                  Color? bg;
                  IconData? icon;
                  Color? textColor;
                  
                  if (provider.showExplanation) {
                    if (isCorrect) {
                      bg = isDark? const Color(0xFF1B5E20) : Colors.green.shade100;
                      textColor = isDark? Colors.white : Colors.black87;
                      icon = Icons.check_circle;
                    } else if (isSelected) {
                      bg = isDark? const Color(0xFF7F1D1D) : Colors.red.shade100;
                      textColor = isDark? Colors.white : Colors.black87;
                      icon = Icons.cancel;
                    } else {
                      bg = isDark? const Color(0xFF1E1E1E) : Colors.white;
                      textColor = isDark? Colors.white70 : Colors.black87;
                    }
                  } else {
                    if (isSelected) {
                      bg = isDark? const Color(0xFF303F9F) : Colors.indigo.shade50;
                      textColor = isDark? Colors.white : Colors.black87;
                    } else {
                      bg = isDark? const Color(0xFF1E1E1E) : Colors.white;
                      textColor = isDark? Colors.white : Colors.black87;
                    }
                  }
                  
                  return Padding(
                    padding: const EdgeInsets.only(bottom: 8),
                    child: Card(
                      color: bg,
                      elevation: isSelected? 3 : 1,
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10), side: BorderSide(color: isSelected? Colors.indigo : Colors.transparent, width: 1.5)),
                      child: ListTile(
                        title: Text(q.options[i], style: TextStyle(fontSize: 15, fontWeight: isSelected? FontWeight.w600 : FontWeight.normal, color: textColor)),
                        leading: CircleAvatar(
                          radius: 16,
                          backgroundColor: isSelected? Colors.indigo : (isDark? const Color(0xFF3A3A3A) : Colors.grey[300]),
                          child: Text(String.fromCharCode(65+i), style: TextStyle(color: isSelected? Colors.white : (isDark? Colors.white : Colors.black87), fontWeight: FontWeight.bold, fontSize: 13)),
                        ),
                        onTap: () => provider.selectAnswer(i),
                        trailing: icon!=null? Icon(icon, color: isCorrect? Colors.greenAccent : Colors.redAccent) : null,
                      ),
                    ),
                  );
                }),
                if (provider.showExplanation)...[
                  const SizedBox(height: 16),
                  Container(
                    width: double.infinity,
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(color: isDark? const Color(0xFF1A237E) : Colors.indigo.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: isDark? Colors.indigo.shade800 : Colors.indigo.shade100)),
                    child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text('Explanation:', style: TextStyle(fontWeight: FontWeight.bold, color: isDark? Colors.white : Colors.indigo[900])),
                      const SizedBox(height: 6),
                      Text(q.explanation, style: TextStyle(fontSize: 14, height: 1.5, color: isDark? Colors.white : Colors.black87)),
                    ]),
                  ),
                  const SizedBox(height: 20),
                ] else ...[
                  const SizedBox(height: 16),
                  Text('👆 Select an answer to continue', style: TextStyle(color: isDark? Colors.white60 : Colors.grey, fontSize: 13)),
                ],
              ],
            ),
          ),
          bottomNavigationBar: SafeArea(
            child: Container(
              padding: EdgeInsets.fromLTRB(12, 8, 12, 12 + MediaQuery.of(context).padding.bottom),
              color: isDark? const Color(0xFF121212) : Colors.white,
              child: Row(
                children: [
                  if (provider.currentIndex > 0) Expanded(child: OutlinedButton.icon(icon: const Icon(Icons.arrow_back), onPressed: provider.previousQuestion, label: const Text('Prev'))),
                  if (provider.currentIndex > 0) const SizedBox(width: 12),
                  Expanded(
                    flex: 2,
                    child: ElevatedButton.icon(
                      icon: Icon(provider.isLastQuestion? Icons.flag : Icons.arrow_forward),
                      style: ElevatedButton.styleFrom(
                        backgroundColor: provider.showExplanation? Colors.indigo : Colors.grey[400],
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
                      label: Text(provider.isLastQuestion? 'Result (${provider.currentIndex+1}/${provider.totalQuestions})' : 'Next (${provider.currentIndex+1}/${provider.totalQuestions})', style: const TextStyle(fontSize: 12)),
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
