package com.vasapps.hllqpprep.core.repository

import com.vasapps.hllqpprep.core.model.Question

object QuestionRepository {


    fun getQuestions(moduleId: String): List<Question> {


        return listOf(

            Question(
                id = 1,
                moduleId = "life",
                moduleName = "Life Insurance",
                topic = "Basics",
                difficulty = "Easy",
                question = "What is the main purpose of life insurance?",
                options = listOf(
                    "Investment growth only",
                    "Financial protection for beneficiaries",
                    "Stock market protection",
                    "Tax avoidance"
                ),
                correctAnswer = 1,
                explanation = "Life insurance provides financial protection to beneficiaries after death."
            ),


            Question(
                id = 2,
                moduleId = "ethics",
                moduleName = "Ethics",
                topic = "Professional Conduct",
                difficulty = "Medium",
                question = "An agent should act in the client's:",
                options = listOf(
                    "Best interest",
                    "Competitor's interest",
                    "Own interest",
                    "Employer's interest only"
                ),
                correctAnswer = 0,
                explanation = "Insurance professionals must act honestly and in the client's best interest."
            )

        )


    }

}
