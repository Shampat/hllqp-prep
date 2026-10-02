import 'dart:async';

import 'package:google_mobile_ads/google_mobile_ads.dart';

class ConsentService {
  ConsentService._();

  static final ConsentService instance = ConsentService._();

  final ConsentInformation _consentInformation = ConsentInformation.instance;

  Future<bool> gatherConsent() async {
    final completer = Completer<bool>();

    final params = ConsentRequestParameters();

    _consentInformation.requestConsentInfoUpdate(
      params,
      () async {
        await ConsentForm.loadAndShowConsentFormIfRequired(
          (formError) async {
            final canRequestAds = await _consentInformation.canRequestAds();
            if (!completer.isCompleted) {
              completer.complete(canRequestAds);
            }
          },
        );
      },
      (formError) async {
        // Consent information could not be refreshed. Google allows the
        // previously cached consent state to determine whether ads may load.
        final canRequestAds = await _consentInformation.canRequestAds();
        if (!completer.isCompleted) {
          completer.complete(canRequestAds);
        }
      },
    );

    return completer.future;
  }

  Future<bool> canRequestAds() {
    return _consentInformation.canRequestAds();
  }

  Future<bool> isPrivacyOptionsRequired() async {
    final status =
        await _consentInformation.getPrivacyOptionsRequirementStatus();

    return status == PrivacyOptionsRequirementStatus.required;
  }

  Future<void> showPrivacyOptions() async {
    final completer = Completer<void>();

    await ConsentForm.showPrivacyOptionsForm(
      (formError) {
        if (!completer.isCompleted) {
          completer.complete();
        }
      },
    );

    return completer.future;
  }
}
