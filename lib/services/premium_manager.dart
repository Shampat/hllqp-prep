import 'package:shared_preferences/shared_preferences.dart';

class PremiumManager {
  static const String _kPremium = 'is_premium_lifetime';
  static const int freeLimit = 15; // 15 free per module

  static Future<bool> isPremium() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getBool(_kPremium) ?? false;
  }

  static Future<void> setPremium(bool value) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(_kPremium, value);
  }

  // Check if user can access question index
  static bool canAccess(int index, bool isPremium) {
    if (isPremium) return true;
    return index < freeLimit;
  }
}
