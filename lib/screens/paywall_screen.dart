import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../services/premium_service.dart';

class PaywallScreen extends StatelessWidget {
  const PaywallScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Upgrade to Pro')),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            const Icon(Icons.workspace_premium, size: 80, color: Colors.orange),
            const SizedBox(height: 16),
            const Text('Unlock All HLLQP Modules', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            const SizedBox(height: 12),
            const Text('• 540+ Questions\n• 100 Mock Q\n• 180 Flashcards\n• No Ads', style: TextStyle(fontSize: 16)),
            const Spacer(),
            ElevatedButton(
              onPressed: () async {
                await context.read<PremiumService>().unlockPro();
                if (context.mounted) Navigator.pop(context);
              },
              style: ElevatedButton.styleFrom(minimumSize: const Size(double.infinity, 50), backgroundColor: Colors.deepOrange),
              child: const Text('Unlock for \$39.99 - TEST'),
            ),
            const SizedBox(height: 12),
            TextButton(onPressed: ()=> Navigator.pop(context), child: const Text('Continue Free (1 module)')),
          ],
        ),
      ),
    );
  }
}
