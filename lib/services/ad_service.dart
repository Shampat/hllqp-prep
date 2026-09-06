import 'package:google_mobile_ads/google_mobile_ads.dart';

class AdService {
  static const String bannerTestId = 'ca-app-pub-3940256099942544/6300978111';

  static BannerAd createBannerAd({required void Function(BannerAd) onLoaded, required void Function() onFailed}) {
    return BannerAd(
      size: AdSize.banner,
      adUnitId: bannerTestId,
      listener: BannerAdListener(
        onAdLoaded: (ad) => onLoaded(ad as BannerAd),
        onAdFailedToLoad: (ad, err) {
          ad.dispose();
          onFailed();
        },
      ),
      request: const AdRequest(),
    )..load();
  }
}
