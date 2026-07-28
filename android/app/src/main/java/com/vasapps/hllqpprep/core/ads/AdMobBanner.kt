package com.vasapps.hllqpprep.core.ads

import android.util.Log
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.ui.viewinterop.AndroidView
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.AdSize
import com.google.android.gms.ads.AdView

@Composable
fun AdMobBanner(modifier: Modifier = Modifier) {
    AndroidView(
        modifier = modifier.fillMaxWidth().height(50.dp),
        factory = { context ->
            try {
                AdView(context).apply {
                    setAdSize(AdSize.BANNER)
                    adUnitId = AdConstants.BANNER_ID
                    loadAd(AdRequest.Builder().build())
                }
            } catch (e: Exception) {
                Log.e("AdMob", "Banner create failed: ${e.message}")
                AdView(context) // return empty view, no crash
            }
        }
    )
}
