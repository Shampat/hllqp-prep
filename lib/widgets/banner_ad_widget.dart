import 'package:flutter/material.dart';
import 'package:google_mobile_ads/google_mobile_ads.dart';
import 'package:provider/provider.dart';

import '../services/ad_service.dart';
import '../services/premium_service.dart';

class BannerAdWidget extends StatefulWidget {
  const BannerAdWidget({super.key});

  @override
  State<BannerAdWidget> createState() => _BannerAdWidgetState();
}

class _BannerAdWidgetState extends State<BannerAdWidget> {
  BannerAd? _ad;
  bool _loaded = false;
  bool _started = false;

  void _loadIfNeeded() {
    if (_started || context.read<PremiumService>().isPro) return;
    _started = true;
    _ad = AdService.createBannerAd(
      onLoaded: (ad) {
        if (!mounted) {
          ad.dispose();
          return;
        }
        setState(() {
          _ad = ad;
          _loaded = true;
        });
      },
      onFailed: () {
        if (!mounted) return;
        setState(() {
          _loaded = false;
          _ad = null;
        });
      },
    );
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    _loadIfNeeded();
  }

  @override
  void dispose() {
    _ad?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final isPro = context.watch<PremiumService>().isPro;

    if (isPro) {
      _ad?.dispose();
      _ad = null;
      _loaded = false;
      return const SizedBox.shrink();
    }

    // Reserve the standard banner height for free users so question/card
    // content does not jump when the ad finishes loading.
    return SizedBox(
      height: AdSize.banner.height.toDouble(),
      child: Center(
        child: _loaded && _ad != null
            ? SizedBox(
                width: _ad!.size.width.toDouble(),
                height: _ad!.size.height.toDouble(),
                child: AdWidget(ad: _ad!),
              )
            : const SizedBox.shrink(),
      ),
    );
  }
}
