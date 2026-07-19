package com.vasapps.hllqpprep.core.repository

import android.content.Context
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import com.vasapps.hllqpprep.core.model.Question

object QuestionRepository {


    fun getQuestions(
        context: Context,
        moduleId: String
    ): List<Question> {


        val fileName =
            when(moduleId) {

                "life" ->
                    "questions/life_questions.json"

                "accident" ->
                    "questions/accident_sickness_questions.json"

                "segregated" ->
                    "questions/segregated_funds_questions.json"

                "annuities" ->
                    "questions/annuities_questions.json"

                "ethics" ->
                    "questions/ethics_questions.json"

                else ->
                    return emptyList()

            }


        val json =
            context.assets
                .open(fileName)
                .bufferedReader()
                .use {
                    it.readText()
                }


        val type =
            object :
                TypeToken<List<Question>>() {}
                .type


        val questions: List<Question> =
            Gson()
                .fromJson(
                    json,
                    type
                )


        return questions

    }

}
