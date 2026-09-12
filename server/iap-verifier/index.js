import express from 'express';
import {GoogleAuth} from 'google-auth-library';

const app = express();
app.use(express.json({limit: '32kb'}));

const PORT = Number(process.env.PORT || 8080);
const PACKAGE_NAME = process.env.ANDROID_PACKAGE_NAME || 'com.vasapps.hllqpprep';
const PRODUCT_ID = process.env.IAP_PRODUCT_ID || 'hllqp_premium_lifetime';

const auth = new GoogleAuth({
  scopes: ['https://www.googleapis.com/auth/androidpublisher'],
});

app.get('/healthz', (_req, res) => {
  res.json({ok: true});
});

app.post('/iap/verify', async (req, res) => {
  try {
    const {
      productId,
      source,
      verificationData,
    } = req.body ?? {};

    if (source !== 'google_play') {
      return res.status(400).json({valid: false, reason: 'unsupported_store'});
    }

    if (productId !== PRODUCT_ID) {
      return res.status(400).json({valid: false, reason: 'wrong_product'});
    }

    if (typeof verificationData !== 'string' || verificationData.length < 10) {
      return res.status(400).json({valid: false, reason: 'missing_purchase_token'});
    }

    const client = await auth.getClient();
    const accessToken = await client.getAccessToken();
    const token = accessToken?.token;

    if (!token) {
      return res.status(503).json({valid: false, reason: 'google_auth_unavailable'});
    }

    const url = new URL(
      `https://androidpublisher.googleapis.com/androidpublisher/v3/applications/${encodeURIComponent(PACKAGE_NAME)}/purchases/products/${encodeURIComponent(PRODUCT_ID)}/tokens/${encodeURIComponent(verificationData)}`,
    );

    const googleResponse = await fetch(url, {
      headers: {
        Authorization: `Bearer ${token}`,
        Accept: 'application/json',
      },
    });

    if (!googleResponse.ok) {
      const status = googleResponse.status;
      return res.status(status === 404 ? 400 : 502).json({
        valid: false,
        reason: status === 404 ? 'purchase_not_found' : 'google_play_error',
      });
    }

    const purchase = await googleResponse.json();

    // ProductPurchase.purchaseState: 0 = purchased, 1 = canceled, 2 = pending.
    const valid = purchase.purchaseState === 0;

    return res.status(valid ? 200 : 400).json({
      valid,
      reason: valid ? 'verified' : 'purchase_not_completed',
      orderId: valid ? purchase.orderId ?? null : undefined,
      acknowledgementState: valid ? purchase.acknowledgementState ?? null : undefined,
    });
  } catch (error) {
    console.error('IAP verification failed', error);
    return res.status(500).json({valid: false, reason: 'verification_error'});
  }
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`IAP verifier listening on port ${PORT}`);
});
