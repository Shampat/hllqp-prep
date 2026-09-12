# HLLQP Google Play IAP Verifier

This service verifies the lifetime product `hllqp_premium_lifetime` with the Google Play Developer API before the Flutter app grants Pro access.

## Endpoint

`POST /iap/verify`

Expected JSON from the app:

```json
{
  "productId": "hllqp_premium_lifetime",
  "purchaseId": "optional-client-value",
  "transactionDate": "optional-client-value",
  "source": "google_play",
  "verificationData": "GOOGLE_PLAY_PURCHASE_TOKEN"
}
```

Success response:

```json
{
  "valid": true,
  "reason": "verified"
}
```

All invalid, canceled, pending, malformed, wrong-product, unsupported-store, or unverifiable purchases return `valid: false`.

## Google Play setup

1. Enable the Google Play Android Developer API in the Google Cloud project used by this service.
2. Create or select a service account.
3. In Google Play Console, give that service account access to the HLLQP app with the permissions required to view orders/purchases.
4. Run this service with Application Default Credentials. Do not store a service-account JSON key in this repository.

The app package is currently `com.vasapps.hllqpprep`. Override it with `ANDROID_PACKAGE_NAME` if that ever changes.

Optional environment variables:

- `ANDROID_PACKAGE_NAME` (default `com.vasapps.hllqpprep`)
- `IAP_PRODUCT_ID` (default `hllqp_premium_lifetime`)
- `PORT` (default `8080`)

## Cloud Run example

From this directory, deploy with your own project, region, and service account:

```bash
gcloud run deploy hllqp-iap-verifier \
  --source . \
  --region YOUR_REGION \
  --service-account YOUR_RUNTIME_SERVICE_ACCOUNT \
  --set-env-vars ANDROID_PACKAGE_NAME=com.vasapps.hllqpprep,IAP_PRODUCT_ID=hllqp_premium_lifetime \
  --allow-unauthenticated
```

The endpoint must be reachable by the mobile app, so the example permits unauthenticated HTTP access. Purchase validity still depends on a Google Play token verified server-side; do not treat client-supplied fields alone as proof of entitlement.

After deployment, build the Flutter app with:

```bash
flutter build appbundle \
  --dart-define=IAP_VERIFY_URL=https://YOUR_SERVICE_URL/iap/verify
```

For closed testing only, the app also supports its intentionally gated test switches. Do not enable them in a production build:

```bash
--dart-define=ALLOW_TEST_UNLOCK=true
--dart-define=ALLOW_UNVERIFIED_IAP=true
```

## Local run

```bash
npm install
npm start
```

Local Google API calls still require Application Default Credentials and Play Console permissions.

## Scope

This verifier currently supports Google Play one-time products. Apple App Store verification should be implemented separately before shipping iOS purchases.
