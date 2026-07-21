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

import com.vasapps.hllqpprep.ui.theme.InsuranceBlue
import com.vasapps.hllqpprep.ui.theme.InsuranceBlueDark
import com.vasapps.hllqpprep.ui.theme.TealProgress


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


    var showJumpDialog by remember {
        mutableStateOf(false)
    }


    var showRestartDialog by remember {
        mutableStateOf(false)
    }


    var jumpCardNumber by remember {
        mutableStateOf("")
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


    if (showJumpDialog) {

        AlertDialog(

            onDismissRequest = {
                showJumpDialog = false
            },

            title = {
                Text("Jump to Card")
            },

            text = {

                OutlinedTextField(
                    value = jumpCardNumber,
                    onValueChange = {
                        jumpCardNumber = it
                    },
                    label = {
                        Text("Card number")
                    }
                )

            },

            confirmButton = {

                Button(

                    onClick = {

                        val target =
                            jumpCardNumber.toIntOrNull()

                        if (
                            target != null &&
                            target > 0 &&
                            target <= questions.size
                        ) {

                            current = target - 1

                            revealed = false


                            if (selectedModule != null) {

                                scope.launch {

                                    ProgressManager.saveFlashcardPosition(
                                        context,
                                        selectedModule!!,
                                        current
                                    )

                                }

                            }

                        }

                        jumpCardNumber = ""

                        showJumpDialog = false

                    }

                ) {

                    Text("Go")

                }

            },

            dismissButton = {

                Button(

                    onClick = {
                        showJumpDialog = false
                    }

                ) {

                    Text("Cancel")

                }

            }

        )

    }


    if (showRestartDialog) {

        AlertDialog(

            onDismissRequest = {
                showRestartDialog = false
            },

            title = {
                Text("Restart Deck?")
            },

            text = {
                Text("Start this flashcard deck again from Card 1?")
            },

            confirmButton = {

                Button(

                    onClick = {

                        current = 0

                        revealed = false


                        if (selectedModule != null) {

                            scope.launch {

                                ProgressManager.saveFlashcardPosition(
                                    context,
                                    selectedModule!!,
                                    0
                                )

                            }

                        }


                        showRestartDialog = false

                    }

                ) {

                    Text("Restart")

                }

            },

            dismissButton = {

                Button(

                    onClick = {
                        showRestartDialog = false
                    }

                ) {

                    Text("Cancel")

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
                            color = InsuranceBlue,
                            style =
                                MaterialTheme.typography.labelLarge
                        )


                        Text(
                            text = question.question,
                            style =
                                MaterialTheme.typography.titleMedium
                        )


                        if (!revealed) {

                            AssistChip(
                                onClick = { },
                                label = {
                                    Text("👆 Tap to reveal")
                                }
                            )

                        }



                        if (revealed) {


                            Text(
                                text = "ANSWER",
                                color = TealProgress,
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
                                color = InsuranceBlueDark,
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



                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.spacedBy(12.dp)
                ) {

                    Button(

                        modifier = Modifier.weight(1f),

                        onClick = {

                            val previousCard =
                                if (current > 0)
                                    current - 1
                                else
                                    questions.size - 1


                            current = previousCard

                            revealed = false


                            if (selectedModule != null) {

                                scope.launch {

                                    ProgressManager.saveFlashcardPosition(
                                        context,
                                        selectedModule!!,
                                        previousCard
                                    )

                                }

                            }

                        }

                    ) {

                        Text("Previous")

                    }



                    Button(

                        modifier = Modifier.weight(1f),

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

                        Text("Next")

                    }

                }


                Row(

                    modifier = Modifier.fillMaxWidth(),

                    horizontalArrangement =
                        Arrangement.SpaceEvenly

                ) {


                    TextButton(

                        onClick = {
                            showJumpDialog = true
                        }

                    ) {

                        Text("Jump to Card")

                    }



                    TextButton(

                        onClick = {
                            showRestartDialog = true
                        }

                    ) {

                        Text("Restart Deck")

                    }


                }


            }

        }

    }

}
