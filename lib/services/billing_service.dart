import 'dart:async';

import 'package:in_app_purchase/in_app_purchase.dart';
import 'premium_service.dart';

class BillingService {
  BillingService._();
  static final BillingService instance = BillingService._();

  static const String productId = 'hllqp_premium_lifetime';

  final InAppPurchase _iap = InAppPurchase.instance;
  StreamSubscription<List<PurchaseDetails>>? _purchaseSubscription;
  bool _available = false;
  bool _initialized = false;

  bool get isAvailable => _available;

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
    return response.productDetails;
  }

  Future<bool> buyPremium(ProductDetails product) async {
    if (!_available || product.id != productId) return false;
    final param = PurchaseParam(productDetails: product);
    return _iap.buyNonConsumable(purchaseParam: param);
  }

  Future<void> restore() async {
    if (_available) {
      await _iap.restorePurchases();
    }
  }

  Future<void> _onPurchaseUpdated(List<PurchaseDetails> purchases) async {
    for (final purchase in purchases) {
      final isCompleted = purchase.status == PurchaseStatus.purchased ||
          purchase.status == PurchaseStatus.restored;

      if (isCompleted && purchase.productID == productId) {
        await PremiumService.instance.setPro(true);
      }

      if (purchase.pendingCompletePurchase &&
          purchase.status != PurchaseStatus.pending) {
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
