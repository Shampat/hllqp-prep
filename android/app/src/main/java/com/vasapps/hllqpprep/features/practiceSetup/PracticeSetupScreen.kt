package com.vasapps.hllqpprep.features.practiceSetup

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp


@Composable
fun PracticeSetupScreen(
    onBack: () -> Unit,
    onStartPractice: () -> Unit,
    onStartScenario: () -> Unit
) {

    Column(

        modifier = Modifier
            .fillMaxSize()
            .padding(24.dp),

        verticalArrangement = Arrangement.spacedBy(16.dp)

    ) {


        Row(
            modifier = Modifier.clickable {
                onBack()
            },

            horizontalArrangement = Arrangement.spacedBy(4.dp)

        ) {

            Icon(
                imageVector = Icons.Default.ArrowBack,
                contentDescription = "Back"
            )

            Text(
                text = "Practice Questions",
                style = MaterialTheme.typography.titleMedium
            )

        }



        Text(
            text = "Choose Practice Style",
            style = MaterialTheme.typography.headlineMedium
        )



        Card(

            modifier = Modifier
                .fillMaxWidth()
                .clickable {
                    onStartPractice()
                },

            colors = CardDefaults.cardColors(
                containerColor = Color(0xFFD6EAF8)
            )

        ) {

            Column(

                modifier = Modifier.padding(20.dp),

                verticalArrangement = Arrangement.spacedBy(8.dp)

            ) {

                Text(
                    text = "⚡ Short Questions",
                    style = MaterialTheme.typography.titleLarge
                )


                Text(
                    text = "Quick recall practice and concept review.",
                    style = MaterialTheme.typography.bodyMedium
                )

            }

        }




        Card(

            modifier = Modifier
                .fillMaxWidth()
                .clickable {
                    onStartScenario()
                },

            colors = CardDefaults.cardColors(
                containerColor = Color(0xFFE8DAEF)
            )

        ) {

            Column(

                modifier = Modifier.padding(20.dp),

                verticalArrangement = Arrangement.spacedBy(8.dp)

            ) {


                Text(
                    text = "📋 Exam Scenarios",
                    style = MaterialTheme.typography.titleLarge
                )


                Text(
                    text = "Real HLLQP-style application questions.",
                    style = MaterialTheme.typography.bodyMedium
                )

            }

        }


    }

}
