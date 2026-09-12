import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/module.dart';
import '../services/premium_service.dart';
import '../widgets/banner_ad_widget.dart';
import 'flashcard_screen.dart';
import 'mock_exam_screen.dart';
import 'paywall_screen.dart';
import 'quiz_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  Color _moduleColor(String hex) {
    final value = int.tryParse(hex.replaceFirst('#', ''), radix: 16) ?? 0x3F51B5;
    return Color(0xFF000000 | value);
  }

  @override
  Widget build(BuildContext context) {
    final premium = context.watch<PremiumService>();
    return Scaffold(
      appBar: AppBar(title: const Text('HLLQP Prep'), centerTitle: true),
      body: SafeArea(
        child: Column(
          children: [
            // Keep the ad outside the scrolling module grid so cards can never
            // move behind or underneath the ad surface.
            const Padding(
              padding: EdgeInsets.symmetric(vertical: 8),
              child: BannerAdWidget(),
            ),
            Expanded(
              child: GridView.builder(
                padding: const EdgeInsets.fromLTRB(12, 4, 12, 12),
                gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 2,
                  crossAxisSpacing: 12,
                  mainAxisSpacing: 12,
                  childAspectRatio: 1.05,
                ),
                itemCount: allModules.length,
                itemBuilder: (context, i) {
                  final module = allModules[i];
                  final fullyFree = premium.isFullyFreeModule(i);
                  final preview = !premium.isPro && !fullyFree;
                  final accent = _moduleColor(module.color);
                  return Card(
                    clipBehavior: Clip.antiAlias,
                    color: Colors.white,
                    child: InkWell(
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (_) => QuizScreen(module: module)),
                        );
                      },
                      child: Padding(
                        padding: const EdgeInsets.all(12),
                        child: Stack(
                          children: [
                            Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Text(module.icon, style: const TextStyle(fontSize: 30)),
                                const SizedBox(height: 8),
                                SizedBox(
                                  width: double.infinity,
                                  child: Text(
                                    module.name,
                                    textAlign: TextAlign.center,
                                    maxLines: 2,
                                    overflow: TextOverflow.ellipsis,
                                    style: const TextStyle(fontSize: 14, fontWeight: FontWeight.w700),
                                  ),
                                ),
                                const SizedBox(height: 5),
                                Text(
                                  preview ? '10 questions free · 50 with Pro' : module.description,
                                  textAlign: TextAlign.center,
                                  maxLines: 2,
                                  overflow: TextOverflow.ellipsis,
                                  style: TextStyle(fontSize: 10, color: Colors.grey.shade700),
                                ),
                              ],
                            ),
                            Positioned(
                              top: 0,
                              left: 0,
                              child: Container(
                                padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                                decoration: BoxDecoration(
                                  color: accent,
                                  borderRadius: BorderRadius.circular(4),
                                ),
                                child: Text(
                                  premium.isPro ? 'PRO' : (fullyFree ? 'FREE' : '10 FREE'),
                                  style: const TextStyle(color: Colors.white, fontSize: 9, fontWeight: FontWeight.bold),
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  );
                },
              ),
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(12, 0, 12, 8),
              child: Row(
                children: [
                  Expanded(
                    child: SizedBox(
                      height: 42,
                      child: ElevatedButton(
                        onPressed: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (_) => premium.isPro
                                  ? const MockExamScreen()
                                  : const PaywallScreen(),
                            ),
                          );
                        },
                        child: Text(
                          premium.isPro ? 'Mock Exam' : 'Mock Exam · PRO',
                          style: const TextStyle(fontSize: 13),
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: SizedBox(
                      height: 42,
                      child: ElevatedButton(
                        onPressed: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(builder: (_) => const FlashcardScreen()),
                          );
                        },
                        child: const Text('Flashcards', style: TextStyle(fontSize: 13)),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
