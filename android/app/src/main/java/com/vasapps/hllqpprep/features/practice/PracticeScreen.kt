package com.vasapps.hllqpprep.features.practice

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.ui.platform.LocalContext
import androidx.compose.runtime.rememberCoroutineScope
import kotlinx.coroutines.launch

import com.vasapps.hllqpprep.core.repository.QuestionRepository
import com.vasapps.hllqpprep.core.utils.ProgressManager


@Composable
fun PracticeScreen(
    mode: PracticeMode,
    onBack: () -> Unit
) {


    val context = LocalContext.current

    val scope = rememberCoroutineScope()

    val questions =
        when (mode) {

            is PracticeMode.Module ->
                QuestionRepository.getQuestions(
                    context,
                    mode.moduleId
                )

            is PracticeMode.MockExam ->
                mode.questions

        }


    var state by remember {
        mutableStateOf(PracticeState())
    }


    var completed by remember {
        mutableStateOf(false)
    }


    var showFinishWarning by remember {
        mutableStateOf(false)
    }



    if (completed) {


        Column(

            modifier = Modifier
                .fillMaxSize()
                .padding(24.dp),

            verticalArrangement =
                Arrangement.spacedBy(20.dp)

        ) {


            Text(
                text =
                    if (mode is PracticeMode.MockExam)
                        "Mock Exam Complete"
                    else
                        "Practice Complete",

                style = MaterialTheme.typography.headlineMedium
            )


            Text(
                text =
                    "Score: ${state.score}/${questions.size}",

                style = MaterialTheme.typography.titleLarge
            )


            Text(
                text =
                    "Accuracy: ${(state.score * 100) / questions.size}%"
            )


            Button(
                onClick = {

                    state = PracticeState()
                    completed = false

                },

                modifier =
                    Modifier.fillMaxWidth()

            ) {

                Text("Retry Practice")

            }


            Button(
                onClick = onBack,

                modifier =
                    Modifier.fillMaxWidth()

            ) {

                Text("Exit Practice")

            }


        }


        return

    }



    if (showFinishWarning) {

        AlertDialog(

            onDismissRequest = {
                showFinishWarning = false
            },

            title = {
                Text("Unanswered Questions")
            },

            text = {

                Text(
                    "Answered: ${state.answeredCount}/${questions.size}"
                )

            },

            confirmButton = {

                Button(
                    onClick = {

                        completed = true
                        showFinishWarning = false

                    }
                ) {

                    Text("Finish Anyway")

                }

            },

            dismissButton = {

                Button(
                    onClick = {

                        val first =
                            state.firstUnanswered(
                                questions.size
                            )

                        if (first != null) {

                            state =
                                state.copy(
                                    currentQuestion = first,
                                    selectedAnswer = null,
                                    answered = false
                                )

                        }

                        showFinishWarning = false

                    }
                ) {

                    Text("Review")

                }

            }

        )

    }



    val question =
        questions[state.currentQuestion]



    Column(

        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp)
            .verticalScroll(rememberScrollState()),

        verticalArrangement =
            Arrangement.spacedBy(12.dp)

    ) {



        Button(
            onClick = onBack
        ) {

            Text("Exit Practice")

        }



        Text(
            text = question.moduleName,
            style = MaterialTheme.typography.headlineSmall
        )


        Text(
            text = "Topic: ${question.topic}    •    Difficulty: ${question.difficulty}",
            style = MaterialTheme.typography.bodyMedium
        )


        Spacer(
            modifier = Modifier.height(8.dp)
        )


        Text(
            text = "Question ${state.currentQuestion + 1} of ${questions.size}",
            style = MaterialTheme.typography.labelLarge
        )


        if (!state.answers.containsKey(state.currentQuestion)) {

            Text(
                text = "⚠ Needs Review",
                style = MaterialTheme.typography.labelLarge
            )

        }


        LinearProgressIndicator(
            progress = {
                (state.currentQuestion + 1).toFloat() /
                questions.size.toFloat()
            },
            modifier = Modifier.fillMaxWidth()
        )


        Text(
            text =
                "Answered: ${state.answeredCount} / ${questions.size}",
            style = MaterialTheme.typography.bodyMedium
        )


        Spacer(
            modifier = Modifier.height(12.dp)
        )



        Card(

            modifier =
                Modifier.fillMaxWidth()

        ) {

            Text(

                text =
                    question.question,

                style =
                    MaterialTheme.typography.headlineSmall,

                modifier =
                    Modifier.padding(20.dp)

            )

        }



        question.options.forEachIndexed { index, option ->


            val isSelected =
                state.selectedAnswer == index


            val isCorrect =
                question.correctAnswer == index


            Card(

                modifier =
                    Modifier.fillMaxWidth(),

                onClick = {

                    if (!state.answered) {

                        state =
                            state.copy(
                                selectedAnswer = index
                            )

                    }

                },

                colors =

                    CardDefaults.cardColors(

                        containerColor =

                            if (
                                state.answered &&
                                isCorrect
                            )

                                androidx.compose.ui.graphics.Color(0xFF2E7D32)

                            else if (
                                state.answered &&
                                isSelected &&
                                !isCorrect
                            )

                                androidx.compose.ui.graphics.Color(0xFFC62828)

                            else if (isSelected)

                                androidx.compose.ui.graphics.Color(0xFF1565C0)

                            else

                                MaterialTheme.colorScheme.surfaceVariant

                    )

            ) {


                Text(

                    text =
                        "${('A'.code + index).toChar()}. $option",

                    modifier =
                        Modifier.padding(20.dp),

                    style =
                        MaterialTheme.typography.bodyLarge

                )

            }


        }




        if (!state.answered) {


            Button(

                enabled =
                    state.selectedAnswer != null,


                onClick = {


                    val correct =
                        state.selectedAnswer ==
                                question.correctAnswer


                    scope.launch {
                        ProgressManager.saveAnswer(
                            context,
                            correct
                        )
                    }


                    state =
                        state.copy(

                            answered = true,

                            score =
                                if(correct)
                                    state.score + 1
                                else
                                    state.score,

                            answers =
                                state.answers +
                                (
                                state.currentQuestion to
                                state.selectedAnswer!!
                                )

                        )

                }

            ) {

                Text("Submit Answer")

            }


        }

        else {


            Text(

                text =
                    if(
                        state.selectedAnswer ==
                        question.correctAnswer
                    )

                        "Correct"

                    else

                        "Incorrect",

                style =
                    MaterialTheme.typography.titleLarge,

                color =
                    if(
                        state.selectedAnswer ==
                        question.correctAnswer
                    )

                        androidx.compose.ui.graphics.Color(0xFF2E7D32)

                    else

                        androidx.compose.ui.graphics.Color(0xFFC62828)

            )


            val answerIsCorrect =
                state.selectedAnswer ==
                        question.correctAnswer


            Text(
                text =
                    if (answerIsCorrect)

                        "✓ Your Answer: " +
                                question.options[
                                    state.selectedAnswer!!
                                ]

                    else

                        "Your Answer: " +
                                question.options[
                                    state.selectedAnswer!!
                                ],

                color =
                    androidx.compose.ui.graphics.Color(0xFFF57C00)
            )


            if (!answerIsCorrect) {

                Text(
                    text =
                        "Correct Answer: " +
                                question.options[
                                    question.correctAnswer
                                ],

                    color =
                        androidx.compose.ui.graphics.Color(0xFF2E7D32)
                )

            }


            Text(
                text =
                    "Explanation: " +
                    question.explanation,

                color =
                    androidx.compose.ui.graphics.Color(0xFF1565C0)
            )


        }





        Row(

            horizontalArrangement =
                Arrangement.SpaceBetween,

            modifier =
                Modifier.fillMaxWidth()

        ) {



            Button(

                enabled =
                    state.currentQuestion > 0,


                onClick = {


                    val previous =
                        state.currentQuestion - 1


                    state =
                        state.copy(

                            currentQuestion =
                                previous,

                            selectedAnswer =
                                state.answers[previous],

                            answered =
                                state.answers.containsKey(previous)

                        )

                }

            ) {

                Text("Previous")

            }





            Button(

                enabled =
                    state.currentQuestion <
                            questions.size - 1
                            || state.answered,


                onClick = {


                    if(
                        state.currentQuestion ==
                        questions.size - 1
                    ) {


                        if (state.answeredCount < questions.size) {

                            showFinishWarning = true

                        } else {

                            completed = true

                        }


                    }

                    else {


                        val next =
                            state.currentQuestion + 1


                        state =
                            state.copy(

                                currentQuestion =
                                    next,

                                selectedAnswer =
                                    state.answers[next],

                                answered =
                                    state.answers.containsKey(next)

                            )

                    }


                }

            ) {


                Text(
                    if(
                        state.currentQuestion ==
                        questions.size - 1
                    )

                        "Finish"

                    else

                        "Next"
                )


            }


        }



        Text(
            text =
                "Score: ${state.score}"
        )


    }


}
