import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../services/premium_service.dart';
import '../widgets/banner_ad_widget.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});
  @override
  Widget build(BuildContext context) {
    final premium = context.watch<PremiumService>();
    return Scaffold(
      appBar: AppBar(title: const Text('HLLQP Prep'), centerTitle: true),
      body: SafeArea(
        child: Column(
          children: [
            Expanded(
              child: GridView.builder(
                padding: const EdgeInsets.all(12),
                gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 2, crossAxisSpacing: 12, mainAxisSpacing: 12, childAspectRatio: 1.1),
                itemCount: 9,
                itemBuilder: (c, i) {
                  final locked = premium.isModuleLocked(i);
                  return Card(
                    color: locked? Colors.grey.shade200 : Colors.white,
                    child: Stack(
                      children: [
                        Center(child: Text('Module ${i+1}\n${locked? '🔒' : 'FREE'}', textAlign: TextAlign.center)),
                        if (!locked) Positioned(top: 6, left: 6, child: Container(padding: const EdgeInsets.symmetric(h:4,v:2), decoration: BoxDecoration(color: Colors.green, borderRadius: BorderRadius.circular(4)), child: const Text('FREE', style: TextStyle(color: Colors.white, fontSize: 10)))),
                        if (locked) const Positioned(top: 6, right: 6, child: Icon(Icons.lock, size: 16)),
                      ],
                    ),
                  );
                },
              ),
            ),
            const BannerAdWidget(),
            const SizedBox(height: 8),
            Padding(
              padding: const EdgeInsets.fromLTRB(12,0,12,8),
              child: Row(
                children: [
                  Expanded(child: SizedBox(height: 42, child: ElevatedButton(onPressed: (){}, child: const Text('Mock Exam', style: TextStyle(fontSize: 13))))),
                  const SizedBox(width: 12),
                  Expanded(child: SizedBox(height: 42, child: ElevatedButton(onPressed: (){}, child: const Text('Flashcards', style: TextStyle(fontSize: 13))))),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
