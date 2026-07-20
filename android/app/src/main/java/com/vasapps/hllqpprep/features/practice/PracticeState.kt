package com.vasapps.hllqpprep.features.practice

data class PracticeState(

    val currentQuestion: Int = 0,

    // current selected option
    val selectedAnswer: Int? = null,

    // submitted status for current question
    val answered: Boolean = false,

    // total correct answers
    val score: Int = 0,

    // store answers for previous questions
    val answers: Map<Int, Int> = emptyMap()

) {

    val answeredCount: Int
        get() = answers.size


    fun firstUnanswered(totalQuestions: Int): Int? {

        return (0 until totalQuestions)
            .firstOrNull { !answers.containsKey(it) }

    }

}
