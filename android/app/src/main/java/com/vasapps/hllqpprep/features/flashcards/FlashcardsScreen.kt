package com.vasapps.hllqpprep.features.flashcards

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import kotlinx.coroutines.launch
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp

import com.vasapps.hllqpprep.core.repository.ModuleRepository
import com.vasapps.hllqpprep.core.repository.QuestionRepository
import com.vasapps.hllqpprep.core.utils.ProgressManager
import com.vasapps.hllqpprep.core.model.Question


@Composable
fun FlashcardsScreen() {

    val context = LocalContext.current


    val scope = rememberCoroutineScope()

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


    var showResumeDialog by remember {
        mutableStateOf(false)
    }


    var resumeCard by remember {
        mutableStateOf<Int?>(null)
    }


    if (showResumeDialog) {


        AlertDialog(

            onDismissRequest = {

                showResumeDialog = false

            },


            title = {

                Text("Continue Flashcards?")

            },


            text = {

                Text(
                    "You stopped at Card ${(resumeCard ?: 0) + 1}."
                )

            },


            confirmButton = {


                Button(

                    onClick = {


                        current =
                            resumeCard ?: 0


                        showResumeDialog =
                            false


                    }

                ) {

                    Text("Continue")

                }


            },


            dismissButton = {


                Button(

                    onClick = {

                        showResumeDialog =
                            false

                    }

                ) {

                    Text("Start Again")

                }

            }

        )


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


                Text(
                    text =
                        "Card ${current + 1} / ${questions.size}",

                    style =
                        MaterialTheme.typography.titleSmall
                )


                LinearProgressIndicator(
                    progress = {
                        (current + 1).toFloat() /
                        questions.size.toFloat()
                    },

                    modifier =
                        Modifier.fillMaxWidth()
                )


                Card(

                    modifier =
                        Modifier
                            .fillMaxWidth()
                            .clickable {

                                revealed = !revealed

                            }

                ) {


                    Column(

                        modifier =
                            Modifier.padding(20.dp),

                        verticalArrangement =
                            Arrangement.spacedBy(12.dp)

                    ) {


                        Text(
                            text = "QUESTION",
                            style =
                                MaterialTheme.typography.labelLarge
                        )


                        Text(
                            text = question.question,
                            style =
                                MaterialTheme.typography.titleMedium
                        )


                        if (!revealed) {

                            Text(
                                text = "Tap card to reveal answer",
                                style =
                                    MaterialTheme.typography.bodyMedium
                            )

                        }



                        if (revealed) {


                            Text(
                                text = "ANSWER",
                                style =
                                    MaterialTheme.typography.labelLarge
                            )


                            Text(
                                text =
                                    question.options[
                                        question.correctAnswer
                                    ]
                            )



                            Text(
                                text = "EXPLANATION",
                                style =
                                    MaterialTheme.typography.labelLarge
                            )


                            Text(
                                text =
                                    question.explanation
                            )

                        }


                    }


                }



                Button(

                    onClick = {


                        val nextCard =
                            (current + 1) %
                            questions.size



                        if (selectedModule != null) {


                            scope.launch {


                                ProgressManager.saveFlashcardPosition(

                                    context,

                                    selectedModule!!,

                                    nextCard

                                )


                            }


                        }



                        current =
                            nextCard



                        revealed = false


                    }

                ) {

                    Text("Next Card")

                }


            }

        }

    }

}
