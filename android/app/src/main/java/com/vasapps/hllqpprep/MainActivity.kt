package com.vasapps.hllqpprep

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import com.vasapps.hllqpprep.navigation.AppNavigation
import com.vasapps.hllqpprep.ui.theme.HLLQPPrepCanadaTheme

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        enableEdgeToEdge()

        setContent {
            HLLQPPrepCanadaTheme {
                AppNavigation()
            }
        }
    }
}
