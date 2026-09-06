import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';

class PremiumProvider extends ChangeNotifier {
  bool _isPremium = false;
  bool get isPremium => _isPremium;

  PremiumProvider() {
    _load();
  }

  Future<void> _load() async {
    final prefs = await SharedPreferences.getInstance();
    _isPremium = prefs.getBool('isPremium')?? false;
    notifyListeners();
  }

  Future<void> setPremium(bool value) async {
    final prefs = await SharedPreferences.getInstance();
    _isPremium = value;
    await prefs.setBool('isPremium', value);
    notifyListeners();
  }

  Future<void> buyPremium() async {
    await setPremium(true);
  }
}
