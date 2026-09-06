import 'package:flutter/material.dart';
import 'package:google_mobile_ads/google_mobile_ads.dart';
import 'package:provider/provider.dart';
import '../services/premium_service.dart';
class BannerAdWidget extends StatefulWidget {
  const BannerAdWidget({super.key});
  @override
  State<BannerAdWidget> createState() => _BannerAdWidgetState();
}
class _BannerAdWidgetState extends State<BannerAdWidget> {
  BannerAd? _ad; bool _loaded = false;
  @override
  void initState() {
    super.initState();
    _ad = BannerAd(
      size: AdSize.banner,
      adUnitId: 'ca-app-pub-3940256099942544/6300978111',
      listener: BannerAdListener(onAdLoaded: (_) => setState(()=> _loaded=true), onAdFailedToLoad: (ad, _)=> ad.dispose()),
      request: const AdRequest(),
    )..load();
  }
  @override
  void dispose(){ _ad?.dispose(); super.dispose(); }
  @override
  Widget build(BuildContext context) {
    if (context.watch<PremiumService>().isPro || !_loaded || _ad==null) return const SizedBox.shrink();
    return Container(margin: const EdgeInsets.only(bottom:6), height: _ad!.size.height.toDouble(), child: AdWidget(ad: _ad!));
  }
}
