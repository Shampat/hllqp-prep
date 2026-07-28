package com.vasapps.hllqpprep.core.ads

import android.content.Context
import android.util.Log
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.LoadAdError
import com.google.android.gms.ads.interstitial.InterstitialAd
import com.google.android.gms.ads.interstitial.InterstitialAdLoadCallback

object InterstitialHelper {
    private var interstitialAd: InterstitialAd? = null
    private var isLoading = false
    private var isShowing = false
    
    fun load(context: Context) {
        if (isLoading || isShowing) return
        isLoading = true
        try {
            val adRequest = AdRequest.Builder().build()
            InterstitialAd.load(context.applicationContext, AdConstants.INTERSTITIAL_ID, adRequest,
                object : InterstitialAdLoadCallback() {
                    override fun onAdLoaded(ad: InterstitialAd) {
                        interstitialAd = ad
                        isLoading = false
                        Log.d("AdMob", "Interstitial loaded")
                    }
                    override fun onAdFailedToLoad(error: LoadAdError) {
                        interstitialAd = null
                        isLoading = false
                        Log.d("AdMob", "Interstitial failed: ${error.message}")
                    }
                })
        } catch (e: Exception) {
            isLoading = false
            Log.e("AdMob", "Load exception: ${e.message}")
        }
    }
    
    fun show(activity: android.app.Activity, onDismissed: () -> Unit = {}) {
        if (isShowing) {
            Log.d("AdMob", "Already showing - skip")
            return
        }
        try {
            val ad = interstitialAd
            if (ad != null) {
                isShowing = true
                ad.fullScreenContentCallback = object : com.google.android.gms.ads.FullScreenContentCallback() {
                    override fun onAdDismissedFullScreenContent() {
                        interstitialAd = null
                        isShowing = false
                        isLoading = false
                        load(activity)
                        onDismissed()
                    }
                    override fun onAdFailedToShowFullScreenContent(e: com.google.android.gms.ads.AdError) {
                        interstitialAd = null
                        isShowing = false
                        isLoading = false
                        load(activity)
                        onDismissed()
                    }
                }
                ad.show(activity)
            } else {
                load(activity)
                onDismissed()
            }
        } catch (e: Exception) {
            isShowing = false
            Log.e("AdMob", "Show failed: ${e.message}")
            onDismissed()
        }
    }
    
    fun isCurrentlyShowing(): Boolean = isShowing
}
