package com.vasapps.hllqpprep.features.mockexam

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp

import com.vasapps.hllqpprep.core.repository.ModuleRepository
import com.vasapps.hllqpprep.core.repository.QuestionRepository
import com.vasapps.hllqpprep.core.model.Question


@Composable
fun MockExamScreen() {

    val context = LocalContext.current

    var selectedModule by remember {
        mutableStateOf<String?>(null)
    }

    var questions by remember {
        mutableStateOf<List<Question>>(emptyList())
    }

    var examStarted by remember {
        mutableStateOf(false)
    }

    var current by remember {
        mutableStateOf(0)
    }

    var score by remember {
        mutableStateOf(0)
    }

    var selectedAnswer by remember {
        mutableStateOf<Int?>(null)
    }


    Column(

        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp)
            .verticalScroll(rememberScrollState()),

        verticalArrangement = Arrangement.spacedBy(16.dp)

    ) {


        Text(
            "Mock Exam",
            style = MaterialTheme.typography.headlineMedium
        )


        if (!examStarted) {


            Text("Select Module")


            ModuleRepository.getModules()
                .forEach { module ->


                    Card(

                        modifier =
                            Modifier
                                .fillMaxWidth()
                                .clickable {


                                    selectedModule = module.id


                                    questions =
                                        QuestionRepository
                                            .getQuestions(
                                                context,
                                                module.id
                                            )
                                            .shuffled()
                                            .take(10)


                                }

                    ) {

                        Text(
                            module.name,
                            modifier =
                                Modifier.padding(20.dp)
                        )

                    }

                }



            if (selectedModule != null) {


                Button(

                    onClick = {

                        examStarted = true

                    }

                ) {

                    Text("Start Exam")

                }

            }


        } else {


            if (current < questions.size) {


                val question =
                    questions[current]


                Text(
                    "Question ${current + 1}/${questions.size}"
                )


                Text(question.question)


                question.options.forEachIndexed { index, option ->


                    Card(

                        modifier =
                            Modifier
                                .fillMaxWidth()
                                .clickable {

                                    selectedAnswer = index

                                }

                    ) {

                        Text(
                            option,
                            modifier =
                                Modifier.padding(16.dp)
                        )

                    }


                }


                Button(

                    onClick = {


                        if (selectedAnswer ==
                            question.correctAnswer) {

                            score++

                        }


                        selectedAnswer = null


                        current++


                    },

                    enabled =
                        selectedAnswer != null

                ) {

                    Text("Next")

                }


            } else {


                Text(
                    "Exam Complete"
                )


                Text(
                    "Score: $score/${questions.size}"
                )

            }


        }


    }

}
