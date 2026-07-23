package com.vasapps.hllqpprep.features.history

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp

import com.vasapps.hllqpprep.core.utils.ProgressManager
import java.text.SimpleDateFormat
import java.util.*


@Composable
fun ExamHistoryScreen(
    onBack: () -> Unit
) {

    val context = LocalContext.current


    val history by
        ProgressManager
            .getExamHistory(context)
            .collectAsState(
                initial = emptyList()
            )



    Column(

        modifier =
            Modifier
                .fillMaxSize()
                .padding(20.dp)
                .verticalScroll(
                    rememberScrollState()
                ),

        verticalArrangement =
            Arrangement.spacedBy(16.dp)

    ) {


        Button(
            onClick = onBack
        ) {

            Text("Back")

        }



        Text(

            text = "Exam History",

            style =
                MaterialTheme.typography.headlineMedium

        )



        if (history.isEmpty()) {


            Text(
                "No mock exams completed yet."
            )


        }



        history.forEach { exam ->


            val percentage =
                if (exam.totalQuestions > 0)
                    (exam.correctAnswers * 100) /
                            exam.totalQuestions
                else
                    0



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
                        "Mock Exam",
                        style =
                            MaterialTheme.typography.titleMedium
                    )


                    Text(
                        "${exam.correctAnswers}/${exam.totalQuestions} correct"
                    )


                    Text(
                        "$percentage% Score"
                    )


                    Text(
                        SimpleDateFormat(
                            "MMM dd, yyyy",
                            Locale.getDefault()
                        ).format(
                            Date(exam.date)
                        )
                    )


                }


            }


        }


    }

}
