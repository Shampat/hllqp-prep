import 'dart:convert';
import 'dart:io';

import 'package:in_app_purchase/in_app_purchase.dart';

class PurchaseVerificationService {
  const PurchaseVerificationService._();

  /// Configure production builds with:
  /// --dart-define=IAP_VERIFY_URL=https://your-api.example.com/iap/verify
  static const String verificationUrl = String.fromEnvironment(
    'IAP_VERIFY_URL',
    defaultValue: '',
  );

  static bool get isConfigured => verificationUrl.trim().isNotEmpty;

  static Future<bool> verify(PurchaseDetails purchase) async {
    if (!isConfigured) return false;

    final uri = Uri.tryParse(verificationUrl);
    if (uri == null || uri.scheme != 'https') return false;

    final client = HttpClient();
    try {
      final request = await client.postUrl(uri);
      request.headers.contentType = ContentType.json;
      request.write(jsonEncode({
        'productId': purchase.productID,
        'purchaseId': purchase.purchaseID,
        'transactionDate': purchase.transactionDate,
        'source': purchase.verificationData.source,
        'verificationData': purchase.verificationData.serverVerificationData,
      }));

      final response = await request.close();
      if (response.statusCode < 200 || response.statusCode >= 300) {
        await response.drain<void>();
        return false;
      }

      final body = await utf8.decoder.bind(response).join();
      final decoded = jsonDecode(body);
      return decoded is Map<String, dynamic> && decoded['valid'] == true;
    } catch (_) {
      return false;
    } finally {
      client.close(force: true);
    }
  }
}
