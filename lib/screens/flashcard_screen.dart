import 'dart:convert';
import 'package:flutter/services.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/question.dart';
import '../models/module.dart';
import '../providers/theme_provider.dart';
import '../services/premium_service.dart';
import '../widgets/banner_ad_widget.dart';

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
  String? loadError;
  ModuleInfo? selectedModule;

  @override
  void initState() {
    super.initState();
    selectedModule = allModules.first;
    WidgetsBinding.instance.addPostFrameCallback((_) => _loadCards(selectedModule!));
  }

  Future<void> _loadCards(ModuleInfo m) async {
    setState(() { isLoading = true; loadError = null; });
    try {
      final data = await rootBundle.loadString(m.assetFile);
      final decoded = json.decode(data);
      if (decoded is! List) throw const FormatException('Expected a JSON array');
      var loaded = decoded.map((e) => Question.fromJson(Map<String, dynamic>.from(e as Map))).toList();
      final moduleIndex = allModules.indexWhere((module) => module.id == m.id);
      final premium = Provider.of<PremiumService>(context, listen: false);
      final limit = moduleIndex < 0 ? null : premium.questionLimitForModule(moduleIndex);
      if (limit != null && loaded.length > limit) {
        loaded.sort((a, b) => a.id.compareTo(b.id));
        loaded = loaded.take(limit).toList();
      }
      loaded.shuffle();
      if (!mounted) return;
      setState(() {
        cards = loaded.take(50).toList();
        index = 0;
        showAnswer = false;
        selectedModule = m;
        isLoading = false;
      });
    } catch (e, st) {
      debugPrint('Flashcard load failed for ${m.id}: $e\n$st');
      if (!mounted) return;
      setState(() {
        cards = [];
        index = 0;
        showAnswer = false;
        selectedModule = m;
        loadError = 'Could not load ${m.name} flashcards.';
        isLoading = false;
      });
    }
  }

  void _toggleAnswer() { if (cards.isNotEmpty) setState(() => showAnswer = !showAnswer); }
  void _prev() { if (index > 0) setState(() { index--; showAnswer = false; }); }
  void _next() { if (index < cards.length - 1) setState(() { index++; showAnswer = false; }); }

  @override
  Widget build(BuildContext context) {
    final isDark = Provider.of<ThemeProvider>(context).isDark;
    final premium = context.watch<PremiumService>();
    final bottomPad = MediaQuery.of(context).padding.bottom;
    final selectedIndex = allModules.indexWhere((m) => m.id == selectedModule?.id);
    final isPreview = !premium.isPro && selectedIndex >= PremiumService.fullyFreeModuleCount;

    return Scaffold(
      backgroundColor: isDark ? const Color(0xFF121212) : const Color(0xFFF5F7FB),
      appBar: AppBar(title: const Text('Flashcards', style: TextStyle(fontWeight: FontWeight.bold)), centerTitle: true),
      body: Column(
        children: [
          const SizedBox(height: 8),
          const BannerAdWidget(),
          const SizedBox(height: 8),
          Container(
            height: 56,
            color: isDark ? const Color(0xFF1E1E1E) : Colors.white,
            child: ListView.separated(
              scrollDirection: Axis.horizontal,
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
              separatorBuilder: (_, __) => const SizedBox(width: 8),
              itemCount: allModules.length,
              itemBuilder: (context, i) {
                final m = allModules[i];
                final sel = selectedModule?.id == m.id;
                final preview = !premium.isPro && i >= PremiumService.fullyFreeModuleCount;
                return ChoiceChip(
                  label: Text('${m.icon} ${m.name}${preview ? ' · 10' : ''}', style: TextStyle(fontSize: 12, color: sel ? Colors.white : (isDark ? Colors.white70 : Colors.black87))),
                  selected: sel,
                  selectedColor: Colors.indigo,
                  backgroundColor: isDark ? const Color(0xFF2A2A2A) : Colors.grey[100],
                  onSelected: (_) => _loadCards(m),
                );
              },
            ),
          ),
          if (isPreview && !isLoading)
            const Padding(
              padding: EdgeInsets.fromLTRB(16, 10, 16, 0),
              child: Text('Free preview: 10 flashcards · Pro unlocks the full module', textAlign: TextAlign.center, style: TextStyle(fontSize: 12, fontWeight: FontWeight.w600)),
            ),
          if (!isLoading && cards.isNotEmpty)
            Padding(
              padding: const EdgeInsets.fromLTRB(16, 12, 16, 0),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Expanded(child: Text(selectedModule?.name ?? '', style: const TextStyle(fontSize: 12, color: Colors.grey, fontWeight: FontWeight.w600))),
                  Text('${index + 1} / ${cards.length}', style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 12)),
                ],
              ),
            ),
          Expanded(
            child: isLoading
                ? const Center(child: CircularProgressIndicator())
                : cards.isEmpty
                    ? Center(child: Padding(padding: const EdgeInsets.all(24), child: Column(mainAxisSize: MainAxisSize.min, children: [Text(loadError ?? 'No cards available', textAlign: TextAlign.center), const SizedBox(height: 12), ElevatedButton(onPressed: selectedModule == null ? null : () => _loadCards(selectedModule!), child: const Text('Retry'))])))
                    : Padding(
                        padding: const EdgeInsets.all(16),
                        child: GestureDetector(
                          onTap: _toggleAnswer,
                          child: Card(
                            elevation: 8,
                            color: isDark ? const Color(0xFF1E1E1E) : Colors.white,
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
                            child: Padding(
                              padding: const EdgeInsets.all(24),
                              child: SingleChildScrollView(
                                child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                                  Text('Q${index + 1}: ${cards[index].question}', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, height: 1.4, color: isDark ? Colors.white : Colors.black87)),
                                  const SizedBox(height: 20),
                                  if (showAnswer) ...[
                                    const Divider(),
                                    const SizedBox(height: 12),
                                    Text('Answer: ${cards[index].options[cards[index].correctAnswer]}', style: TextStyle(fontSize: 16, color: isDark ? Colors.white : Colors.green[800], fontWeight: FontWeight.bold)),
                                    const SizedBox(height: 16),
                                    Text(cards[index].explanation, style: TextStyle(fontSize: 14, height: 1.5, color: isDark ? Colors.white70 : Colors.black87)),
                                  ] else Text('Tap to reveal answer', style: TextStyle(color: isDark ? Colors.white54 : Colors.grey)),
                                ]),
                              ),
                            ),
                          ),
                        ),
                      ),
          ),
          if (cards.isNotEmpty)
            SafeArea(
              child: Container(
                color: isDark ? const Color(0xFF121212) : Colors.white,
                padding: EdgeInsets.fromLTRB(16, 8, 16, 16 + bottomPad),
                child: Column(mainAxisSize: MainAxisSize.min, children: [
                  SizedBox(width: double.infinity, child: ElevatedButton(onPressed: _toggleAnswer, child: Text(showAnswer ? 'Hide Answer' : 'Show Answer'))),
                  const SizedBox(height: 12),
                  Row(children: [
                    Expanded(child: ElevatedButton(onPressed: index > 0 ? _prev : null, child: const Text('Previous'))),
                    const SizedBox(width: 12),
                    Text('${index + 1}/${cards.length}', style: const TextStyle(fontWeight: FontWeight.bold)),
                    const SizedBox(width: 12),
                    Expanded(child: ElevatedButton(onPressed: index < cards.length - 1 ? _next : null, child: Text(index == cards.length - 1 ? 'Done' : 'Next'))),
                  ]),
                ]),
              ),
            ),
        ],
      ),
    );
  }
}
