package com.vasapps.hllqpprep.features.practice

import androidx.compose.foundation.layout.Row
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
import com.vasapps.hllqpprep.core.model.ExamResult


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


    var showResumeDialog by remember {
        mutableStateOf(false)
    }


    var resumeIndex by remember {
        mutableStateOf<Int?>(null)
    }


    var resumeTime by remember {
        mutableStateOf<Long?>(null)
    }


    var resumeChecked by remember {
        mutableStateOf(false)
    }



    fun saveExamHistoryIfNeeded() {

        if (mode is PracticeMode.MockExam) {

            scope.launch {

                ProgressManager.saveExamResult(
                    context,
                    ExamResult(
                        date = System.currentTimeMillis(),
                        totalQuestions = questions.size,
                        correctAnswers = state.score
                    )
                )

            }

        }

    }



    LaunchedEffect(Unit) {

        if (mode is PracticeMode.Module) {

            ProgressManager
                .getPracticeState(context)
                .collect { savedState ->


                    state =
                        state.copy(

                            currentQuestion =
                                savedState.first,

                            score =
                                savedState.second,

                            answers =
                                savedState.third

                        )


                    if (
                        !resumeChecked &&
                        savedState.first > 0
                    ) {

                        resumeChecked = true

                        resumeIndex =
                            savedState.first

                        showResumeDialog =
                            true

                    }

                }

        }

    }



    if (showResumeDialog) {


        AlertDialog(

            onDismissRequest = {

                showResumeDialog = false

            },


            title = {

                Text("Continue Practice?")

            },


            text = {

                Text(
                    buildString {

                        append(
                            "You stopped at Question ${(resumeIndex ?: 0) + 1}."
                        )

                        resumeTime?.let {

                            val days =
                                ((System.currentTimeMillis() - it)
                                    /
                                    (1000 * 60 * 60 * 24))

                            append(
                                "\n\nLast studied: $days days ago."
                            )

                        }

                    }
                )

            },


            confirmButton = {


                Button(

                    onClick = {


                        state =
                            state.copy(

                                currentQuestion =
                                    resumeIndex ?: 0

                            )


                        showResumeDialog = false


                    }

                ) {

                    Text("Continue")

                }


            },


            dismissButton = {


                Button(

                    onClick = {


                        scope.launch {

                            ProgressManager
                                .clearPracticePosition(context)

                        }


                        state =
                            PracticeState()


                        resumeIndex = null


                        showResumeDialog = false


                    }

                ) {


                    Text("Start Again")

                }


            }


        )


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

                        saveExamHistoryIfNeeded()

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
            text = question.topic,
            style = MaterialTheme.typography.titleMedium
        )


        Text(
            text = "Difficulty: ${question.difficulty}",
            style = MaterialTheme.typography.bodyMedium
        )


        Spacer(
            modifier = Modifier.height(8.dp)
        )


        Card(
            modifier = Modifier.fillMaxWidth()
        ) {

            Column(
                modifier = Modifier.padding(16.dp),
                verticalArrangement = Arrangement.spacedBy(8.dp)
            ) {


                Text(
                    text = "Question ${state.currentQuestion + 1} of ${questions.size}",
                    style = MaterialTheme.typography.titleSmall
                )


                Text(
                    text =
                        "Answered: ${state.answeredCount} / ${questions.size}",

                    style =
                        MaterialTheme.typography.bodyMedium
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

            }

        }


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


                Row(
                    modifier =
                        Modifier.padding(20.dp),

                    horizontalArrangement =
                        Arrangement.spacedBy(12.dp)

                ) {

                    Text(
                        text =
                            "${('A'.code + index).toChar()}",

                        style =
                            MaterialTheme.typography.titleMedium
                    )


                    Text(
                        text = option,

                        style =
                            MaterialTheme.typography.bodyLarge
                    )

                }

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



                    if (!correct) {


                        scope.launch {


                            ProgressManager.saveWrongAnswer(
                                context,
                                question.id
                            )


                        }


                    } else {


                        scope.launch {


                            ProgressManager.removeWrongAnswer(
                                context,
                                question.id
                            )


                        }


                    }



                    scope.launch {
                        ProgressManager.saveAnswer(
                            context,
                            correct
                        )
                    }


                    val newScore =
                        if (correct)
                            state.score + 1
                        else
                            state.score


                    val newAnswers =
                        state.answers +
                        (
                            state.currentQuestion to
                            state.selectedAnswer!!
                        )


                    state =
                        state.copy(

                            answered = true,

                            score = newScore,

                            answers = newAnswers

                        )


                    if (mode is PracticeMode.Module) {

                        scope.launch {

                            ProgressManager.savePracticeState(
                                context,
                                mode.moduleId,
                                state.currentQuestion,
                                newScore,
                                newAnswers
                            )

                        }

                    }

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



                        if (mode is PracticeMode.Module) {

                            scope.launch {

                                ProgressManager.savePracticePosition(
                                    context,
                                    mode.moduleId,
                                    next
                                )

                            }

                        }



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
