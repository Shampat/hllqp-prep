package com.vasapps.hllqpprep.features.flashcards

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
fun FlashcardsScreen() {

    val context = LocalContext.current

    var selectedModule by remember {
        mutableStateOf<String?>(null)
    }

    var questions by remember {
        mutableStateOf<List<Question>>(emptyList())
    }

    var current by remember {
        mutableStateOf(0)
    }

    var revealed by remember {
        mutableStateOf(false)
    }


    Column(

        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp)
            .verticalScroll(rememberScrollState()),

        verticalArrangement = Arrangement.spacedBy(16.dp)

    ) {


        Text(
            "Flashcards",
            style = MaterialTheme.typography.headlineMedium
        )


        if (selectedModule == null) {


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

                                }

                    ) {

                        Text(
                            text = module.name,
                            modifier = Modifier.padding(20.dp)
                        )

                    }


                }


        } else {


            if (questions.isNotEmpty()) {


                val question =
                    questions[current]


                Card(

                    modifier =
                        Modifier.fillMaxWidth()
                            .clickable {

                                revealed = !revealed

                            }

                ) {


                    Column(
                        modifier =
                            Modifier.padding(20.dp)
                    ) {


                        Text(question.question)


                        Spacer(
                            Modifier.height(16.dp)
                        )


                        if (revealed) {

                            Text(
                                "Answer: " +
                                question.options[
                                    question.correctAnswer
                                ]
                            )


                            Spacer(
                                Modifier.height(10.dp)
                            )


                            Text(
                                question.explanation
                            )

                        }


                    }


                }



                Button(

                    onClick = {

                        current =
                            (current + 1) %
                            questions.size

                        revealed = false

                    }

                ) {

                    Text("Next Card")

                }


            }

        }

    }

}
