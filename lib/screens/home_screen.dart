import 'package:flutter/material.dart';
import '../models/module.dart';
import 'quiz_screen.dart';
import 'mock_exam_screen.dart';
import 'flashcard_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('HLLQP Prep - Canada', style: TextStyle(fontSize:16)), backgroundColor: Colors.indigo, foregroundColor: Colors.white),
      body: Column(
        children: [
          Expanded(
            child: GridView.builder(
              padding: const EdgeInsets.all(8),
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2, childAspectRatio: 1.1, crossAxisSpacing: 8, mainAxisSpacing: 8),
              itemCount: allModules.length,
              itemBuilder: (context, index) {
                final m = allModules[index];
                return Card(
                  child: InkWell(
                    onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => QuizScreen(module: m))),
                    child: Center(
                      child: Padding(
                        padding: const EdgeInsets.all(8),
                        child: Column(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Text(m.icon, style: const TextStyle(fontSize: 28)),
                            const SizedBox(height: 8),
                            Text(m.name, textAlign: TextAlign.center, style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 12), maxLines: 3),
                          ],
                        ),
                      ),
                    ),
                  ),
                );
              },
            ),
          ),
          SafeArea(
            child: Padding(
              padding: const EdgeInsets.all(8),
              child: Row(children: [
                Expanded(child: ElevatedButton(onPressed: ()=> Navigator.push(context, MaterialPageRoute(builder: (_)=> const MockExamScreen())), style: ElevatedButton.styleFrom(backgroundColor: Colors.indigo, foregroundColor: Colors.white), child: const Text('📝 Mock Exam (100Q)', style: TextStyle(fontSize:12)))),
                const SizedBox(width:8),
                Expanded(child: ElevatedButton(onPressed: ()=> Navigator.push(context, MaterialPageRoute(builder: (_)=> const FlashcardScreen())), style: ElevatedButton.styleFrom(backgroundColor: Colors.deepOrange, foregroundColor: Colors.white), child: const Text('🃏 Flashcards', style: TextStyle(fontSize:12)))),
              ]),
            ),
          ),
        ],
      ),
    );
  }
}
