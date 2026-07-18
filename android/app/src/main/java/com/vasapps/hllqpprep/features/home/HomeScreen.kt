package com.vasapps.hllqpprep.features.home

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp


@Composable
fun HomeScreen(
    onPracticeClick: () -> Unit
) {

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(24.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {


        Text(
            text = "HLLQP Prep Canada",
            style = MaterialTheme.typography.headlineMedium
        )


        Text(
            text = "Prepare for your Canadian insurance licensing exam"
        )


        Button(
            onClick = onPracticeClick,
            modifier = Modifier.fillMaxWidth()
        ) {

            Text("Practice Questions")

        }


        Card {

            Text(
                text = "Mock Exams",
                modifier = Modifier.padding(20.dp)
            )

        }


        Card {

            Text(
                text = "Flashcards",
                modifier = Modifier.padding(20.dp)
            )

        }

    }

}
