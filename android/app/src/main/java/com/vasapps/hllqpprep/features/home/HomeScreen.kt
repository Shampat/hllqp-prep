package com.vasapps.hllqpprep.features.home

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.MenuBook
import androidx.compose.material.icons.filled.Quiz
import androidx.compose.material.icons.filled.Style
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.platform.LocalContext
import com.vasapps.hllqpprep.core.utils.ProgressManager
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@Composable
fun HomeScreen(
    onPracticeClick: () -> Unit,
    onMockExamClick: () -> Unit,
    onFlashcardsClick: () -> Unit
) {

    val context = LocalContext.current

    val progress =
        ProgressManager.getProgress(context)
            .collectAsState(initial = Pair(0, 0))

    val attempted = progress.value.first
    val correct = progress.value.second

    val accuracy =
        if (attempted > 0)
            (correct * 100) / attempted
        else
            0


    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp)
            .verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {

        Text(
            text = "HLLQP Prep Canada",
            style = MaterialTheme.typography.headlineMedium
        )

        Text(
            text = "Prepare for your Canadian Insurance Licensing Exam",
            style = MaterialTheme.typography.bodyLarge
        )

        Card(
            modifier = Modifier.fillMaxWidth()
        ) {

            Column(
                modifier = Modifier.padding(20.dp),
                verticalArrangement = Arrangement.spacedBy(8.dp)
            ) {

                Text(
                    "Your Progress",
                    style = MaterialTheme.typography.titleMedium
                )

                Text(
                    "Questions Answered: $attempted"
                )

                Text(
                    "Accuracy: $accuracy%"
                )

            }

        }


        Text(
            text = "Study Tools",
            style = MaterialTheme.typography.titleLarge
        )

        Card(
            modifier = Modifier.fillMaxWidth(),
            onClick = onPracticeClick,
            colors = CardDefaults.cardColors()
        ) {
            Column(Modifier.padding(20.dp)) {
                Icon(Icons.Default.MenuBook, contentDescription = null)
                Text(
                    "Practice Questions",
                    style = MaterialTheme.typography.titleMedium
                )
                Text("Practice by module with instant explanations.")
            }
        }

        Card(
            modifier = Modifier.fillMaxWidth(),
            onClick = onMockExamClick,
            colors = CardDefaults.cardColors()
        ) {
            Column(Modifier.padding(20.dp)) {
                Icon(Icons.Default.Quiz, contentDescription = null)
                Text(
                    "Mock Exam",
                    style = MaterialTheme.typography.titleMedium
                )
                Text("Simulate the HLLQP exam.")
            }
        }

        Card(
            modifier = Modifier.fillMaxWidth(),
            onClick = onFlashcardsClick,
            colors = CardDefaults.cardColors()
        ) {
            Column(Modifier.padding(20.dp)) {
                Icon(Icons.Default.Style, contentDescription = null)
                Text(
                    "Flashcards",
                    style = MaterialTheme.typography.titleMedium
                )
                Text("Quick review of important concepts.")
            }
        }
    }
}
