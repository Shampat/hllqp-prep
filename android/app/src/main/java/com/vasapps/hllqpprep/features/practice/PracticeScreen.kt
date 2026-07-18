package com.vasapps.hllqpprep.features.practice

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

import com.vasapps.hllqpprep.core.repository.QuestionRepository


@Composable
fun PracticeScreen(
    selectedModule: String,
    onBack: () -> Unit
) {


    val questions = QuestionRepository.getQuestions()


    var state by remember {
        mutableStateOf(PracticeState())
    }


    val question = questions[state.currentQuestion]


    Column(

        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp),

        verticalArrangement = Arrangement.spacedBy(12.dp)

    ) {


        Button(
            onClick = onBack
        ) {

            Text("Exit Practice")

        }



        Text(
            text = "Question ${state.currentQuestion + 1}/${questions.size}",
            style = MaterialTheme.typography.labelLarge
        )


        Text(
            text = selectedModule.uppercase(),
            style = MaterialTheme.typography.titleMedium
        )


        Text(
            text = question.question,
            style = MaterialTheme.typography.headlineSmall
        )



        question.options.forEachIndexed { index, option ->


            Button(

                enabled = !state.answered,

                onClick = {

                    state = state.copy(
                        selectedAnswer = index
                    )

                },

                modifier = Modifier.fillMaxWidth(),

                colors =
                    if (state.selectedAnswer == index)

                        ButtonDefaults.buttonColors(
                            containerColor =
                                MaterialTheme.colorScheme.primary
                        )

                    else

                        ButtonDefaults.buttonColors()

            ) {

                Text(option)

            }


        }



        if (!state.answered) {


            Button(

                enabled = state.selectedAnswer != null,

                onClick = {


                    val correct =
                        state.selectedAnswer == question.correctAnswer


                    state = state.copy(

                        answered = true,

                        score =
                            if (correct)
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
                    if (
                        state.selectedAnswer ==
                        question.correctAnswer
                    )

                        "Correct"

                    else

                        "Incorrect",

                style =
                    MaterialTheme.typography.titleLarge
            )


            Text(
                text = question.explanation
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


                    state = state.copy(

                        currentQuestion = previous,

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
                            questions.size - 1,

                onClick = {

                    val next =
                        state.currentQuestion + 1


                    state = state.copy(

                        currentQuestion = next,

                        selectedAnswer =
                            state.answers[next],

                        answered =
                            state.answers.containsKey(next)

                    )

                }

            ) {

                Text("Next")

            }


        }



        Text(
            text = "Score: ${state.score}"
        )


    }

}
