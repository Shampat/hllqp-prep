import 'dart:convert';
import 'package:flutter/services.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/question.dart';
import '../models/module.dart';
import '../providers/theme_provider.dart';

class FlashcardScreen extends StatefulWidget {
  const FlashcardScreen({super.key});
  @override
  State<FlashcardScreen> createState() => _FlashcardScreenState();
}

class _FlashcardScreenState extends State<FlashcardScreen> {
  List<Question> cards = [];
  int index = 0;
  bool showAnswer = false;
  bool isLoading = true;
  ModuleInfo? selectedModule;

  String flashcardAssetFor(ModuleInfo m) => 'assets/flashcards/${m.id}_flashcards.json';

  @override
  void initState() {
    super.initState();
    selectedModule = allModules.first;
    _loadCards(selectedModule!);
  }

  Future<void> _loadCards(ModuleInfo m) async {
    setState(() { isLoading = true; });
    try {
      String data;
      try {
        data = await rootBundle.loadString(flashcardAssetFor(m));
      } catch (_) {
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

  void _toggleAnswer() => setState(() => showAnswer =!showAnswer);
  void _prev() { if (index > 0) setState(() { index--; showAnswer = false; }); }
  void _next() { if (index < cards.length - 1) setState(() { index++; showAnswer = false; }); }

  @override
  Widget build(BuildContext context) {
    final isDark = Provider.of<ThemeProvider>(context).isDark;
    final bottomPad = MediaQuery.of(context).padding.bottom;

    return Scaffold(
      backgroundColor: isDark? const Color(0xFF121212) : const Color(0xFFF5F7FB),
      appBar: AppBar(
        title: const Text('Flashcards', style: TextStyle(fontWeight: FontWeight.bold)),
        centerTitle: true,
        backgroundColor: isDark? const Color(0xFF1A1A2E) : Colors.white,
        foregroundColor: isDark? Colors.white : Colors.black87,
        elevation: 0,
      ),
      body: Column(
        children: [
          Container(
            height: 56,
            color: isDark? const Color(0xFF1E1E1E) : Colors.white,
            child: ListView.separated(
              scrollDirection: Axis.horizontal,
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
              separatorBuilder: (_, __) => const SizedBox(width: 8),
              itemCount: allModules.length,
              itemBuilder: (context, i) {
                final m = allModules[i];
                final sel = selectedModule?.id == m.id;
                return ChoiceChip(
                  label: Text('${m.icon} ${m.name}', style: TextStyle(fontSize: 12, color: sel? Colors.white : (isDark? Colors.white70 : Colors.black87))),
                  selected: sel,
                  selectedColor: Colors.indigo,
                  backgroundColor: isDark? const Color(0xFF2A2A2A) : Colors.grey[100],
                  onSelected: (_) => _loadCards(m),
                );
              },
            ),
          ),
          if (!isLoading && cards.isNotEmpty)
            Padding(
              padding: const EdgeInsets.fromLTRB(16, 12, 16, 0),
              child: Column(
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(selectedModule?.name?? '', style: const TextStyle(fontSize: 12, color: Colors.grey, fontWeight: FontWeight.w600)),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                        decoration: BoxDecoration(color: Colors.indigo, borderRadius: BorderRadius.circular(20)),
                        child: Text('${index + 1} / ${cards.length}', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 12)),
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),
                  ClipRRect(
                    borderRadius: BorderRadius.circular(10),
                    child: LinearProgressIndicator(value: (index + 1) / cards.length, minHeight: 6, backgroundColor: Colors.grey[200], valueColor: const AlwaysStoppedAnimation(Colors.indigo)),
                  ),
                ],
              ),
            ),
          Expanded(
            child: isLoading
              ? const Center(child: CircularProgressIndicator())
                : cards.isEmpty
                  ? const Center(child: Text('No cards'))
                    : Padding(
                        padding: const EdgeInsets.all(16),
                        child: GestureDetector(
                          onTap: _toggleAnswer,
                          child: Card(
                            elevation: 8,
                            color: isDark? const Color(0xFF1E1E1E) : Colors.white,
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
                            child: Padding(
                              padding: const EdgeInsets.all(24),
                              child: SingleChildScrollView(
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text("Q${index + 1}: ${cards[index].question}", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, height: 1.4, color: isDark? Colors.white : Colors.black87)),
                                    const SizedBox(height: 20),
                                    if (showAnswer)...[
                                      const Divider(),
                                      const SizedBox(height: 12),
                                      Container(
                                        padding: const EdgeInsets.all(12),
                                        decoration: BoxDecoration(color: isDark? const Color(0xFF1B5E20) : Colors.green[50], borderRadius: BorderRadius.circular(12)),
                                        child: Text("Answer: ${cards[index].options[cards[index].correctAnswer]}", style: TextStyle(fontSize: 16, color: isDark? Colors.white : Colors.green[800], fontWeight: FontWeight.bold)),
                                      ),
                                      const SizedBox(height: 16),
                                      Text(cards[index].explanation, style: TextStyle(fontSize: 14, height: 1.5, color: isDark? Colors.white70 : Colors.black87)),
                                    ] else
                                      Text("Tap to reveal answer", style: TextStyle(color: isDark? Colors.white54 : Colors.grey)),
                                  ],
                                ),
                              ),
                            ),
                          ),
                        ),
                      ),
          ),
          // ONLY THIS PART FIXED - Samsung nav fix
          SafeArea(
            child: Container(
              color: isDark? const Color(0xFF121212) : Colors.white,
              padding: EdgeInsets.fromLTRB(16, 8, 16, 16 + bottomPad),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  SizedBox(width: double.infinity, child: ElevatedButton(onPressed: _toggleAnswer, style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 14)), child: Text(showAnswer? "Hide Answer" : "Show Answer"))),
                  const SizedBox(height: 12),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Expanded(child: ElevatedButton(onPressed: index > 0? _prev : null, style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 14)), child: const Text("Previous"))),
                      const SizedBox(width: 12),
                      Text("${index + 1}/${cards.length}", style: TextStyle(fontWeight: FontWeight.bold, color: isDark? Colors.white : Colors.black87)),
                      const SizedBox(width: 12),
                      Expanded(child: ElevatedButton(onPressed: index < cards.length - 1? _next : null, style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 14)), child: Text(index == cards.length - 1? "Done" : "Next"))),
                    ],
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
