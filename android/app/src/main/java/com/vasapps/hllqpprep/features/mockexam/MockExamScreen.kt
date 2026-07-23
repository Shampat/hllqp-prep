package com.vasapps.hllqpprep.features.mockexam

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
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

        verticalArrangement =
            Arrangement.spacedBy(20.dp)

    ) {


        Text(
            text = "HLLQP Mock Exam",

            style =
                MaterialTheme.typography.headlineMedium
        )



        Text(
            text =
                "Test your readiness under exam conditions.",

            style =
                MaterialTheme.typography.bodyLarge
        )



        Card(

            modifier =
                Modifier.fillMaxWidth(),

            colors =
                CardDefaults.cardColors(
                containerColor = Color(0xFFE8F5E9)
            )

        ) {

            Column(

                modifier =
                    Modifier.padding(20.dp),

                verticalArrangement =
                    Arrangement.spacedBy(8.dp)

            ) {


                Text(
                    text = "QUESTION BANK",

                    style =
                        MaterialTheme.typography.labelLarge
                )


                Text(
                    text =
                        "$totalQuestions",

                    style =
                        MaterialTheme.typography.headlineLarge
                )


                Text(
                    text =
                        "Available Questions"
                )

            }

        }



        Card(

            modifier =
                Modifier.fillMaxWidth(),

            colors = CardDefaults.cardColors(
                containerColor = Color(0xFFFFF8E1)
            )

        ) {

            Column(

                modifier =
                    Modifier.padding(20.dp),

                verticalArrangement =
                    Arrangement.spacedBy(8.dp)

            ) {


                Text(
                    text = "EXAM FORMAT",

                    style =
                        MaterialTheme.typography.labelLarge
                )


                Text(
                    text =
                        "10 Random Questions",

                    style =
                        MaterialTheme.typography.titleLarge
                )


                Text(
                    text =
                        "Practice with a realistic exam-style session."

                )

            }

        }




        Button(

            modifier =
                Modifier.fillMaxWidth(),

            onClick =
                onStartExam

        ) {


            Text(
                "Start Mock Exam"
            )

        }

    }

}
