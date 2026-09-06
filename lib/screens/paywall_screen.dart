import 'package:flutter/material.dart';
import 'package:in_app_purchase/in_app_purchase.dart';
import '../services/billing_service.dart';
import '../services/premium_manager.dart';

class PaywallScreen extends StatefulWidget {
  const PaywallScreen({super.key});
  @override
  State<PaywallScreen> createState() => _PaywallScreenState();
}

class _PaywallScreenState extends State<PaywallScreen> {
  final BillingService _billing = BillingService();
  ProductDetails? _product;
  bool _loading = true;

  @override
  void initState() {
    super.initState();
    _init();
  }

  Future<void> _init() async {
    await _billing.init();
    final products = await _billing.getProducts();
    setState(() {
      if (products.isNotEmpty) _product = products.first;
      _loading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(title: const Text('Unlock Premium'), backgroundColor: Colors.black),
      body: _loading ? const Center(child: CircularProgressIndicator()) : Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            const SizedBox(height: 20),
            const Icon(Icons.workspace_premium, size: 80, color: Colors.amber),
            const SizedBox(height: 20),
            const Text('Pass HLLQP in 1st Attempt', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.white)),
            const SizedBox(height: 10),
            const Text('One attempt costs \$125 + 2 months wait. Unlock all for one time \$39.99', textAlign: TextAlign.center, style: TextStyle(color: Colors.white70)),
            const SizedBox(height: 30),
            _feature('1800+ Questions with Explanations'),
            _feature('Full Mock 100Q Exams'),
            _feature('500+ Flashcards'),
            _feature('Remove Ads - AdMob Banner Removed'),
            const Spacer(),
            SizedBox(
              width: double.infinity,
              child: ElevatedButton(
                style: ElevatedButton.styleFrom(backgroundColor: Colors.blue, padding: const EdgeInsets.all(16)),
                onPressed: () async {
                  if (_product != null) await _billing.buyPremium(_product!);
                },
                child: Text(_product != null ? 'Unlock Lifetime - ${_product!.price}' : 'Unlock Lifetime - \$39.99', style: const TextStyle(fontSize: 18)),
              ),
            ),
            TextButton(onPressed: () => _billing.restore(), child: const Text('Restore Purchase')),
            const SizedBox(height: 10),
          ],
        ),
      ),
    );
  }

  Widget _feature(String t) => Padding(
    padding: const EdgeInsets.symmetric(vertical: 6),
    child: Row(children: [const Icon(Icons.check_circle, color: Colors.green, size: 20), const SizedBox(width: 10), Text(t, style: const TextStyle(color: Colors.white))]),
  );
}
