package com.vasapps.hllqpprep

import android.os.Bundle
import android.util.Log
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import com.vasapps.hllqpprep.navigation.AppNavigation
import com.vasapps.hllqpprep.ui.theme.HLLQPPrepCanadaTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        // CRASH-PROOF AdMob init - runs safely in background
        try {
            Thread {
                try {
                    com.google.android.gms.ads.MobileAds.initialize(this) {}
                    com.vasapps.hllqpprep.core.ads.InterstitialHelper.load(this)
                    Log.d("AdMob", "AdMob init OK")
                } catch (e: Exception) {
                    Log.e("AdMob", "AdMob init failed: ${e.message}")
                }
            }.start()
        } catch (e: Exception) {
            Log.e("AdMob", "Thread start failed: ${e.message}")
        }

        enableEdgeToEdge()
        setContent {
            HLLQPPrepCanadaTheme {
                AppNavigation()
            }
        }
    }
}
