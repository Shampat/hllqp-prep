import 'package:in_app_purchase/in_app_purchase.dart';
import 'premium_manager.dart';

class BillingService {
  static const String productId = 'hllqp_premium_lifetime';
  final InAppPurchase _iap = InAppPurchase.instance;
  bool _available = false;

  Future<void> init() async {
    _available = await _iap.isAvailable();
    if (_available) {
      final Stream<List<PurchaseDetails>> purchaseUpdated = _iap.purchaseStream;
      purchaseUpdated.listen(_onPurchaseUpdated);
    }
  }

  Future<List<ProductDetails>> getProducts() async {
    final ProductDetailsResponse response = await _iap.queryProductDetails({productId});
    return response.productDetails;
  }

  Future<void> buyPremium(ProductDetails product) async {
    final PurchaseParam param = PurchaseParam(productDetails: product);
    await _iap.buyNonConsumable(purchaseParam: param);
  }

  Future<void> restore() async {
    await _iap.restorePurchases();
  }

  void _onPurchaseUpdated(List<PurchaseDetails> purchases) async {
    for (var p in purchases) {
      if (p.status == PurchaseStatus.purchased || p.status == PurchaseStatus.restored) {
        if (p.productID == productId) {
          await PremiumManager.setPremium(true);
          if (p.pendingCompletePurchase) {
            await _iap.completePurchase(p);
          }
        }
      }
    }
  }
}
