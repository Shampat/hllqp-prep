import 'package:flutter/material.dart';
import 'package:in_app_purchase/in_app_purchase.dart';
import 'package:provider/provider.dart';

import '../services/billing_service.dart';
import '../services/premium_service.dart';

class PaywallScreen extends StatefulWidget {
  const PaywallScreen({super.key});

  @override
  State<PaywallScreen> createState() => _PaywallScreenState();
}

class _PaywallScreenState extends State<PaywallScreen> {
  ProductDetails? _product;
  bool _loading = true;
  bool _busy = false;
  String? _message;

  @override
  void initState() { super.initState(); _loadProduct(); }

  Future<void> _loadProduct() async {
    final billing = BillingService.instance;
    if (!billing.isAvailable) {
      if (!mounted) return;
      setState(() { _loading = false; _message = 'Store billing is unavailable on this device.'; });
      return;
    }
    try {
      final products = await billing.getProducts();
      if (!mounted) return;
      setState(() {
        _product = products.isEmpty ? null : products.first;
        _loading = false;
        if (products.isEmpty) _message = 'The Pro product is not available from the store.';
      });
    } catch (_) {
      if (!mounted) return;
      setState(() { _loading = false; _message = 'Could not load the Pro product. Please try again.'; });
    }
  }

  Future<void> _buy() async {
    final product = _product;
    if (product == null || _busy) return;
    setState(() { _busy = true; _message = null; });
    try {
      final started = await BillingService.instance.buyPremium(product);
      if (!mounted) return;
      setState(() {
        _busy = false;
        _message = started
            ? 'Purchase started. Complete it in the store to unlock Pro.'
            : (BillingService.instance.canProcessPurchases ? 'The purchase could not be started.' : 'Purchase verification is not configured for this build.');
      });
    } catch (_) {
      if (!mounted) return;
      setState(() { _busy = false; _message = 'The purchase could not be started.'; });
    }
  }

  Future<void> _restore() async {
    if (_busy) return;
    setState(() { _busy = true; _message = null; });
    try {
      final started = await BillingService.instance.restore();
      if (!mounted) return;
      setState(() {
        _busy = false;
        _message = started ? 'Restore requested. Verified purchases will unlock automatically.' : 'Purchase verification is not configured for this build.';
      });
    } catch (_) {
      if (!mounted) return;
      setState(() { _busy = false; _message = 'Could not restore purchases.'; });
    }
  }

  Future<void> _testUnlock() async {
    if (_busy || !PremiumService.allowTestUnlock) return;
    setState(() => _busy = true);
    try {
      await context.read<PremiumService>().unlockPro();
      if (!mounted) return;
      Navigator.pop(context);
    } finally {
      if (mounted) setState(() => _busy = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    final premium = context.watch<PremiumService>();
    final billing = BillingService.instance;
    final product = _product;
    return Scaffold(
      appBar: AppBar(title: const Text('Upgrade to Pro')),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(20),
          child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
            const Icon(Icons.workspace_premium, size: 80, color: Colors.orange),
            const SizedBox(height: 16),
            const Text('Unlock Complete HLLQP Prep', textAlign: TextAlign.center, style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            const SizedBox(height: 12),
            const Text('Free includes 190 questions: all 60 Life, all 60 Accident & Sickness, plus 10 questions from each other module.', textAlign: TextAlign.center, style: TextStyle(fontSize: 14, height: 1.4)),
            const SizedBox(height: 16),
            const Text('Pro includes:\n• All 540 practice questions\n• Full flashcards across every module\n• 100-question comprehensive mock\n• No banner ads', style: TextStyle(fontSize: 16, height: 1.5)),
            const SizedBox(height: 28),
            if (premium.isPro)
              const Text('Pro is already unlocked on this device.', textAlign: TextAlign.center, style: TextStyle(fontWeight: FontWeight.w600))
            else if (_loading)
              const Center(child: CircularProgressIndicator())
            else ...[
              ElevatedButton(
                onPressed: _busy || product == null || !billing.canProcessPurchases ? null : _buy,
                style: ElevatedButton.styleFrom(minimumSize: const Size(double.infinity, 50), backgroundColor: Colors.deepOrange, foregroundColor: Colors.white),
                child: Text(product == null ? 'Pro unavailable' : 'Unlock Pro — ${product.price}'),
              ),
              const SizedBox(height: 10),
              OutlinedButton(onPressed: _busy || !billing.canProcessPurchases ? null : _restore, child: const Text('Restore Purchases')),
            ],
            if (_message != null) ...[
              const SizedBox(height: 12),
              Text(_message!, textAlign: TextAlign.center, style: TextStyle(color: Theme.of(context).colorScheme.error)),
            ],
            if (PremiumService.allowTestUnlock) ...[
              const SizedBox(height: 16),
              const Divider(),
              const SizedBox(height: 8),
              OutlinedButton.icon(onPressed: _busy ? null : _testUnlock, icon: const Icon(Icons.science_outlined), label: const Text('Closed-test unlock')),
              const SizedBox(height: 6),
              const Text('Visible only in builds created with ALLOW_TEST_UNLOCK=true.', textAlign: TextAlign.center, style: TextStyle(fontSize: 11, color: Colors.grey)),
            ],
            const SizedBox(height: 12),
            TextButton(onPressed: () => Navigator.pop(context), child: const Text('Continue with 190 free questions')),
          ]),
        ),
      ),
    );
  }
}
