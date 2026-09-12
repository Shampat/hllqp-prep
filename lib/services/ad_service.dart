import 'package:google_mobile_ads/google_mobile_ads.dart';

class AdService {
  static const String _testBannerId =
      'ca-app-pub-3940256099942544/6300978111';

  /// Production builds can supply a real banner unit with:
  /// --dart-define=ADMOB_BANNER_ID=ca-app-pub-xxxxxxxxxxxxxxxx/yyyyyyyyyy
  static const String _configuredBannerId = String.fromEnvironment(
    'ADMOB_BANNER_ID',
    defaultValue: '',
  );

  static String get bannerAdUnitId =>
      _configuredBannerId.trim().isEmpty ? _testBannerId : _configuredBannerId;

  static bool get isUsingTestAd => bannerAdUnitId == _testBannerId;

  static Future<void> initialize() async {
    await MobileAds.instance.initialize();
  }

  static BannerAd createBannerAd({
    required void Function(BannerAd) onLoaded,
    required void Function() onFailed,
  }) {
    return BannerAd(
      size: AdSize.banner,
      adUnitId: bannerAdUnitId,
      listener: BannerAdListener(
        onAdLoaded: (ad) => onLoaded(ad as BannerAd),
        onAdFailedToLoad: (ad, _) {
          ad.dispose();
          onFailed();
        },
      ),
      request: const AdRequest(),
    )..load();
  }
}
