import 'dart:async';

import 'package:in_app_purchase/in_app_purchase.dart';
import 'premium_service.dart';

typedef PurchaseVerificationCallback = Future<bool> Function(
  PurchaseDetails purchase,
);

class BillingService {
  BillingService._();
  static final BillingService instance = BillingService._();

  static const String productId = 'hllqp_premium_lifetime';

  /// Closed-test escape hatch for store sandbox testing only. Production
  /// builds should provide a server-backed verifier instead.
  static const bool allowUnverifiedStorePurchases = bool.fromEnvironment(
    'ALLOW_UNVERIFIED_IAP',
    defaultValue: false,
  );

  final InAppPurchase _iap = InAppPurchase.instance;
  StreamSubscription<List<PurchaseDetails>>? _purchaseSubscription;
  PurchaseVerificationCallback? _verifier;
  bool _available = false;
  bool _initialized = false;

  bool get isAvailable => _available;
  bool get hasVerifier => _verifier != null;
  bool get canProcessPurchases =>
      _available && (hasVerifier || allowUnverifiedStorePurchases);

  void setVerifier(PurchaseVerificationCallback verifier) {
    _verifier = verifier;
  }

  Future<void> init() async {
    if (_initialized) return;
    _initialized = true;

    _available = await _iap.isAvailable();
    if (!_available) return;

    _purchaseSubscription = _iap.purchaseStream.listen(
      _onPurchaseUpdated,
      onError: (_) {},
    );
  }

  Future<List<ProductDetails>> getProducts() async {
    if (!_available) return const [];
    final response = await _iap.queryProductDetails({productId});
    return response.productDetails
        .where((product) => product.id == productId)
        .toList(growable: false);
  }

  Future<bool> buyPremium(ProductDetails product) async {
    if (!canProcessPurchases || product.id != productId) return false;
    final param = PurchaseParam(productDetails: product);
    return _iap.buyNonConsumable(purchaseParam: param);
  }

  Future<bool> restore() async {
    if (!canProcessPurchases) return false;
    await _iap.restorePurchases();
    return true;
  }

  Future<bool> _verifyPurchase(PurchaseDetails purchase) async {
    final verifier = _verifier;
    if (verifier != null) {
      try {
        return await verifier(purchase);
      } catch (_) {
        return false;
      }
    }

    if (!allowUnverifiedStorePurchases) return false;

    // Closed-test fallback only. Presence of store verification data is not a
    // substitute for server verification and must never be used for production.
    return purchase.verificationData.serverVerificationData.isNotEmpty;
  }

  Future<void> _onPurchaseUpdated(List<PurchaseDetails> purchases) async {
    for (final purchase in purchases) {
      if (purchase.productID != productId) continue;

      final isCompleted = purchase.status == PurchaseStatus.purchased ||
          purchase.status == PurchaseStatus.restored;

      if (!isCompleted) continue;

      final verified = await _verifyPurchase(purchase);
      if (!verified) {
        // Fail closed: do not grant entitlement or complete an unverified
        // transaction. A configured verifier can process it on redelivery.
        continue;
      }

      await PremiumService.instance.setPro(true);

      if (purchase.pendingCompletePurchase) {
        await _iap.completePurchase(purchase);
      }
    }
  }

  Future<void> dispose() async {
    await _purchaseSubscription?.cancel();
    _purchaseSubscription = null;
    _initialized = false;
  }
}
