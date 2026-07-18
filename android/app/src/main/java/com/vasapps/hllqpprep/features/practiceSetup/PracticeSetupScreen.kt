package com.vasapps.hllqpprep.features.practiceSetup

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp


@Composable
fun PracticeSetupScreen(
    onBack: () -> Unit,
    onStartPractice: () -> Unit
) {

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(24.dp),
        verticalArrangement = Arrangement.spacedBy(20.dp)
    ) {


        Button(
            onClick = onBack
        ) {

            Text("Back")

        }


        Text(
            text = "Practice Setup",
            style = MaterialTheme.typography.headlineMedium
        )


        Text(
            text = "Choose your exam settings"
        )


        Button(
            onClick = onStartPractice,
            modifier = Modifier.fillMaxWidth()
        ) {

            Text("Start Practice")

        }

    }
}
