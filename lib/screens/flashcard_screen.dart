import 'dart:convert';
import 'package:flutter/services.dart';
import 'package:flutter/material.dart';
import '../models/question.dart';
import '../models/module.dart';

class FlashcardScreen extends StatefulWidget {
  const FlashcardScreen({super.key});
  @override
  State<FlashcardScreen> createState() => _FlashcardScreenState();
}

class _FlashcardScreenState extends State<FlashcardScreen> with TickerProviderStateMixin {
  List<Question> cards = [];
  int index = 0;
  bool showAnswer = false;
  bool isLoading = true;
  ModuleInfo? selectedModule;
  late AnimationController _flipCtrl;

  // Map module id -> dedicated flashcard asset
  String flashcardAssetFor(ModuleInfo m) {
    return 'assets/flashcards/${m.id}_flashcards.json';
  }

  @override
  void initState() {
    super.initState();
    selectedModule = allModules.first;
    _flipCtrl = AnimationController(vsync: this, duration: const Duration(milliseconds: 300));
    _loadCards(selectedModule!);
  }

  @override
  void dispose() {
    _flipCtrl.dispose();
    super.dispose();
  }

  Future<void> _loadCards(ModuleInfo m) async {
    setState(() { isLoading = true; });
    try {
      // Try dedicated flashcards first
      String asset = flashcardAssetFor(m);
      String data;
      try {
        data = await rootBundle.loadString(asset);
      } catch (_) {
        // Fallback to questions if flashcard file missing
        data = await rootBundle.loadString(m.assetFile);
      }
      final list = json.decode(data) as List;
      final all = list.map((e) => Question.fromJson(e)).toList();
      all.shuffle();
      setState(() {
        cards = all.take(50).toList();
        index = 0;
        showAnswer = false;
        selectedModule = m;
        isLoading = false;
      });
    } catch (e) {
      setState(() { isLoading = false; });
    }
  }

  void _toggleAnswer() {
    setState(() {
      showAnswer =!showAnswer;
      if (showAnswer) _flipCtrl.forward(); else _flipCtrl.reverse();
    });
  }

  void _prev() {
    if (index > 0) setState(() { index--; showAnswer = false; _flipCtrl.reset(); });
  }

  void _next() {
    if (index < cards.length - 1) setState(() { index++; showAnswer = false; _flipCtrl.reset(); });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF5F7FB),
      appBar: AppBar(title: const Text('Flashcards', style: TextStyle(fontWeight: FontWeight.bold)), centerTitle: true, backgroundColor: Colors.white, elevation: 0, foregroundColor: Colors.black87),
      body: Column(children: [
        Container(height: 56, color: Colors.white, child: ListView.separated(scrollDirection: Axis.horizontal, padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8), separatorBuilder: (_, __) => const SizedBox(width: 8), itemCount: allModules.length, itemBuilder: (context, i) {
          final m = allModules[i];
          final sel = selectedModule?.id == m.id;
          return ChoiceChip(label: Text('${m.icon} ${m.name}', style: TextStyle(fontSize: 12, color: sel? Colors.white : Colors.black87)), selected: sel, selectedColor: Colors.indigo, backgroundColor: Colors.grey[100], onSelected: (_) => _loadCards(m));
        })),
        if (!isLoading && cards.isNotEmpty) Padding(padding: const EdgeInsets.fromLTRB(16,12,16,0), child: Column(children: [
          Row(mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [Text('${selectedModule?.name}', style: const TextStyle(fontSize: 12, color: Colors.grey, fontWeight: FontWeight.w600)), Container(padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4), decoration: BoxDecoration(color: Colors.indigo, borderRadius: BorderRadius.circular(20)), child: Text('${index+1} / ${cards.length}', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 12)))]),
          const SizedBox(height: 8),
          ClipRRect(borderRadius: BorderRadius.circular(10), child: LinearProgressIndicator(value: (index+1)/cards.length, minHeight: 6, backgroundColor: Colors.grey[200], valueColor: const AlwaysStoppedAnimation(Colors.indigo))),
        ])),
        Expanded(child: isLoading? const Center(child: CircularProgressIndicator()) : cards.isEmpty? const Center(child: Text('No cards')) : Padding(padding: const EdgeInsets.all(16), child: GestureDetector(onTap: _toggleAnswer, child: Card(elevation: 8, shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)), child: Padding(padding: const EdgeInsets.all(24), child: SingleChildScrollView(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text("Q${index+1}: ${cards[index].question}", style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, height: 1.4)),
          const SizedBox(height: 20),
          if (showAnswer)...[
            const Divider(), const SizedBox(height: 12),
            Container(padding: const EdgeInsets.all(12), decoration: BoxDecoration(color: Colors.green[50], borderRadius: BorderRadius.circular(12)), child: Text("Answer: ${cards[index].options[cards[index].correctAnswer]}", style: TextStyle(fontSize: 16, color: Colors.green[800], fontWeight: FontWeight.bold))),
            const SizedBox(height: 16),
            Text(cards[index].explanation, style: const TextStyle(fontSize: 14, height: 1.5)),
          ] else const Text("Tap to reveal answer", style: TextStyle(color: Colors.grey)),
        ])))))),
        Padding(padding: const EdgeInsets.symmetric(horizontal: 16), child: SizedBox(width: double.infinity, child: ElevatedButton(onPressed: _toggleAnswer, child: Text(showAnswer? "Hide Answer" : "Show Answer")))),
        Padding(padding: const EdgeInsets.fromLTRB(16,12,16,24), child: Row(mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [
          ElevatedButton(onPressed: index>0? _prev : null, child: const Text("Previous")),
          Text("${index+1}/${cards.length}", style: const TextStyle(fontWeight: FontWeight.bold)),
          ElevatedButton(onPressed: index<cards.length-1? _next : null, child: Text(index==cards.length-1? "Done" : "Next")),
        ])),
      ]),
    );
  }
}
