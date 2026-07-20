package com.vasapps.hllqpprep.features.mockexam

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import com.vasapps.hllqpprep.core.repository.QuestionRepository

@Composable
fun MockExamScreen(
    onStartExam: () -> Unit
) {

    val context = LocalContext.current

    val totalQuestions =
        QuestionRepository
            .getAllQuestions(context)
            .size

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp),
        verticalArrangement = Arrangement.spacedBy(20.dp)
    ) {

        Text(
            text = "Mock Exam",
            style = MaterialTheme.typography.headlineMedium
        )


        Card(
            modifier = Modifier.fillMaxWidth()
        ) {

            Column(
                modifier = Modifier.padding(20.dp)
            ) {

                Text("Question Bank")

                Text(
                    "$totalQuestions Questions Available",
                    style = MaterialTheme.typography.titleLarge
                )

            }

        }


        Button(
            modifier = Modifier.fillMaxWidth(),
            onClick = onStartExam
        ) {

            Text("Start 10 Question Mock Exam")

        }

    }

}
