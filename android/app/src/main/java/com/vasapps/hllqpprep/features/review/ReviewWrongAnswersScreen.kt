
package com.vasapps.hllqpprep.features.review

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp

import com.vasapps.hllqpprep.core.repository.QuestionRepository
import com.vasapps.hllqpprep.core.utils.ProgressManager
import kotlinx.coroutines.launch


@Composable
fun ReviewWrongAnswersScreen(
    onBack: () -> Unit
) {


    val context = LocalContext.current

    val scope = rememberCoroutineScope()


    val wrongIds by
        ProgressManager
            .getWrongAnswers(context)
            .collectAsState(
                initial = emptySet()
            )


    val questions =
        QuestionRepository
            .getAllQuestions(context)
            .filter {
                wrongIds.contains(it.id)
            }


    var current by remember {
        mutableStateOf(0)
    }



    Column(

        modifier =
            Modifier
                .fillMaxSize()
                .padding(20.dp),

        verticalArrangement =
            Arrangement.spacedBy(16.dp)

    ) {



        Button(
            onClick = onBack
        ) {

            Text("Back")

        }



        Text(

            text =
                "Review Mistakes",

            style =
                MaterialTheme.typography.headlineMedium

        )



        if (questions.isEmpty()) {


            Text(
                "No mistakes to review. Great job!"
            )


        } else {


            val question =
                questions[current]



            Text(
                "Question ${current + 1} / ${questions.size}"
            )



            Card(

                modifier =
                    Modifier.fillMaxWidth(),

                colors =
                    CardDefaults.cardColors(
                        containerColor = Color(0xFFFFF3E0)
                    )

            ) {


                Column(

                    modifier =
                        Modifier.padding(20.dp),

                    verticalArrangement =
                        Arrangement.spacedBy(12.dp)

                ) {


                    Text(

                        question.question,

                        style =
                            MaterialTheme.typography.titleMedium

                    )



                    Text(

                        "Correct Answer: " +
                                question.options[
                                    question.correctAnswer
                                ]

                    )



                    Text(

                        "Explanation: " +
                                question.explanation

                    )


                }


            }



            Row(

                modifier =
                    Modifier.fillMaxWidth(),

                horizontalArrangement =
                    Arrangement.SpaceBetween

            ) {



                Button(

                    onClick = {


                        scope.launch {


                            ProgressManager.removeWrongAnswer(

                                context,

                                question.id

                            )


                        }


                    }

                ) {

                    Text("Remove")

                }



                Button(

                    onClick = {


                        current =
                            (current + 1) %
                            questions.size


                    }

                ) {

                    Text("Next")

                }


            }


        }


    }


}
