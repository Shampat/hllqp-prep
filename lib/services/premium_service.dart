import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';
class PremiumService extends ChangeNotifier {
  static final PremiumService instance = PremiumService._();
  PremiumService._();
  static late SharedPreferences _prefs;
  bool _isPro = false;
  bool get isPro => _isPro;
  static Future<void> init() async {
    _prefs = await SharedPreferences.getInstance();
    instance._isPro = _prefs.getBool('is_pro')?? false;
  }
  bool isModuleLocked(int i) => _isPro? false : i > 1;
  Future<void> unlockPro() async { _isPro=true; await _prefs.setBool('is_pro', true); notifyListeners(); }
}
