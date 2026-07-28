package com.vasapps.hllqpprep.core.ads

import androidx.compose.foundation.layout.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext

@Composable
fun BannerScaffold(
    content: @Composable () -> Unit
) {
    val context = LocalContext.current
    var isPremium by remember { mutableStateOf(false) }
    
    LaunchedEffect(Unit) {
        PremiumManager.isPremiumFlow(context).collect { isPremium = it }
    }

    Column(modifier = Modifier.fillMaxSize()) {
        Box(modifier = Modifier.weight(1f)) {
            content()
        }
        if (!isPremium) {
            AdMobBanner(modifier = Modifier.fillMaxWidth())
        }
    }
}
