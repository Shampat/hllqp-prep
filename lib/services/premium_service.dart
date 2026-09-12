import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';

class PremiumService extends ChangeNotifier {
  static final PremiumService instance = PremiumService._();
  PremiumService._();

  static const String _premiumKey = 'is_pro';
  static const List<String> _legacyPremiumKeys = [
    'is_premium_lifetime',
    'isPremium',
  ];

  static const int fullyFreeModuleCount = 2;
  static const int freePreviewQuestionCount = 10;

  /// Explicitly opt in for closed-test builds with:
  /// --dart-define=ALLOW_TEST_UNLOCK=true
  static const bool allowTestUnlock = bool.fromEnvironment(
    'ALLOW_TEST_UNLOCK',
    defaultValue: false,
  );

  static late SharedPreferences _prefs;
  bool _isPro = false;

  bool get isPro => _isPro;

  static Future<void> init() async {
    _prefs = await SharedPreferences.getInstance();

    final canonical = _prefs.getBool(_premiumKey) ?? false;
    final legacyUnlocked = _legacyPremiumKeys.any(
      (key) => _prefs.getBool(key) ?? false,
    );

    instance._isPro = canonical || legacyUnlocked;

    if (legacyUnlocked && !canonical) {
      await _prefs.setBool(_premiumKey, true);
    }

    for (final key in _legacyPremiumKeys) {
      await _prefs.remove(key);
    }
  }

  bool isFullyFreeModule(int index) => index < fullyFreeModuleCount;

  /// All study modules can be opened. Free users receive the complete first
  /// two modules and a stable 10-question preview of every remaining module.
  bool isModuleLocked(int index) => false;

  int? questionLimitForModule(int index) {
    if (_isPro || isFullyFreeModule(index)) return null;
    return freePreviewQuestionCount;
  }

  Future<void> setPro(bool value) async {
    if (_isPro == value) return;
    _isPro = value;
    await _prefs.setBool(_premiumKey, value);
    notifyListeners();
  }

  /// Closed-testing convenience path. This is unavailable unless the build
  /// explicitly opts in with ALLOW_TEST_UNLOCK=true.
  Future<void> unlockPro() async {
    if (!allowTestUnlock) {
      throw StateError('Test premium unlock is disabled for this build.');
    }
    await setPro(true);
  }
}
