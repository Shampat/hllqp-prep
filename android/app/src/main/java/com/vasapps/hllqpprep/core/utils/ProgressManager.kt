package com.vasapps.hllqpprep.core.utils

import android.content.Context
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.intPreferencesKey
import androidx.datastore.preferences.core.longPreferencesKey
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.core.stringSetPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import com.vasapps.hllqpprep.core.model.ExamResult

private val Context.dataStore by preferencesDataStore(
    name = "user_progress"
)

object ProgressManager {

    private val TOTAL_ATTEMPTED =
        intPreferencesKey("total_attempted")

    private val TOTAL_CORRECT =
        intPreferencesKey("total_correct")


    private val PRACTICE_MODULE =
        stringPreferencesKey("practice_module")


    private val PRACTICE_INDEX =
        intPreferencesKey("practice_question_index")


    private val PRACTICE_SCORE =
        intPreferencesKey("practice_score")


    private val PRACTICE_ANSWERS =
        stringPreferencesKey("practice_answers")


    private val PRACTICE_TIME =
        longPreferencesKey("practice_last_time")


    private val FLASHCARD_MODULE =
        stringPreferencesKey("flashcard_module")


    private val FLASHCARD_INDEX =
        intPreferencesKey("flashcard_index")


    private val WRONG_QUESTIONS =
        stringSetPreferencesKey("wrong_questions")


    private val EXAM_HISTORY =
        stringPreferencesKey("exam_history")


    suspend fun saveAnswer(
        context: Context,
        correct: Boolean
    ) {

        context.dataStore.edit { prefs ->

            val attempted =
                prefs[TOTAL_ATTEMPTED] ?: 0

            val correctCount =
                prefs[TOTAL_CORRECT] ?: 0


            prefs[TOTAL_ATTEMPTED] =
                attempted + 1


            if (correct) {
                prefs[TOTAL_CORRECT] =
                    correctCount + 1
            }
        }
    }


    fun getProgress(
        context: Context
    ): Flow<Pair<Int, Int>> {

        return context.dataStore.data.map { prefs ->

            Pair(
                prefs[TOTAL_ATTEMPTED] ?: 0,
                prefs[TOTAL_CORRECT] ?: 0
            )
        }
    }


    suspend fun savePracticePosition(
        context: Context,
        moduleId: String,
        questionIndex: Int
    ) {

        context.dataStore.edit { prefs ->

            prefs[PRACTICE_MODULE] = moduleId

            prefs[PRACTICE_INDEX] = questionIndex

            prefs[PRACTICE_TIME] =
                System.currentTimeMillis()

        }

    }



    fun getPracticeModule(
        context: Context
    ): Flow<Pair<String?, Int?>> {

        return context.dataStore.data.map { prefs ->

            Pair(
                prefs[PRACTICE_MODULE],
                prefs[PRACTICE_INDEX]
            )

        }

    }



    suspend fun savePracticeState(
        context: Context,
        moduleId: String,
        questionIndex: Int,
        score: Int,
        answers: Map<Int, Int>
    ) {

        context.dataStore.edit { prefs ->

            prefs[PRACTICE_MODULE] = moduleId

            prefs[PRACTICE_INDEX] = questionIndex

            prefs[PRACTICE_SCORE] = score


            prefs[PRACTICE_ANSWERS] =
                answers.entries.joinToString(",") {
                    "${it.key}:${it.value}"
                }

        }

    }



    fun getPracticeState(
        context: Context
    ): Flow<Triple<Int, Int, Map<Int, Int>>> {

        return context.dataStore.data.map { prefs ->


            val score =
                prefs[PRACTICE_SCORE] ?: 0


            val index =
                prefs[PRACTICE_INDEX] ?: 0


            val answers =
                prefs[PRACTICE_ANSWERS]
                    ?.split(",")
                    ?.filter { it.contains(":") }
                    ?.associate {

                        val parts = it.split(":")

                        parts[0].toInt() to parts[1].toInt()

                    }
                    ?: emptyMap()


            Triple(
                index,
                score,
                answers
            )

        }

    }



    suspend fun clearProgress(
        context: Context
    ) {

        context.dataStore.edit { prefs ->

            prefs.remove(TOTAL_ATTEMPTED)

            prefs.remove(TOTAL_CORRECT)

            prefs.remove(PRACTICE_MODULE)

            prefs.remove(PRACTICE_INDEX)

            prefs.remove(PRACTICE_SCORE)

            prefs.remove(PRACTICE_ANSWERS)

            prefs.remove(PRACTICE_TIME)

            prefs.remove(WRONG_QUESTIONS)

        }

    }




    suspend fun clearPracticePosition(
        context: Context
    ) {

        context.dataStore.edit { prefs ->

            prefs.remove(PRACTICE_MODULE)

            prefs.remove(PRACTICE_INDEX)

        }

    }


    suspend fun saveFlashcardPosition(
        context: Context,
        moduleId: String,
        index: Int
    ) {

        context.dataStore.edit { prefs ->

            prefs[FLASHCARD_MODULE] =
                moduleId


            prefs[FLASHCARD_INDEX] =
                index

        }

    }



    fun getFlashcardPosition(
        context: Context
    ): Flow<Pair<String?, Int?>> {

        return context.dataStore.data.map { prefs ->

            Pair(
                prefs[FLASHCARD_MODULE],
                prefs[FLASHCARD_INDEX]
            )

        }

    }





    suspend fun saveWrongAnswer(
        context: Context,
        questionId: Int
    ) {

        context.dataStore.edit { prefs ->


            val current =
                prefs[WRONG_QUESTIONS]
                    ?: emptySet()


            prefs[WRONG_QUESTIONS] =
                current + questionId.toString()

        }

    }



    fun getWrongAnswers(
        context: Context
    ): Flow<Set<Int>> {


        return context.dataStore.data.map { prefs ->


            prefs[WRONG_QUESTIONS]
                ?.map { it.toInt() }
                ?.toSet()
                ?: emptySet()


        }

    }




    suspend fun saveExamResult(
        context: Context,
        result: ExamResult
    ) {

        context.dataStore.edit { prefs ->

            val gson = Gson()

            val existing =
                prefs[EXAM_HISTORY]
                    ?: "[]"


            val type =
                object : TypeToken<MutableList<ExamResult>>() {}.type


            val history =
                gson.fromJson<MutableList<ExamResult>>(
                    existing,
                    type
                )


            history.add(0, result)


            prefs[EXAM_HISTORY] =
                gson.toJson(history)

        }

    }



    fun getExamHistory(
        context: Context
    ): Flow<List<ExamResult>> {

        return context.dataStore.data.map { prefs ->

            val gson = Gson()

            val json =
                prefs[EXAM_HISTORY]
                    ?: "[]"


            val type =
                object : TypeToken<List<ExamResult>>() {}.type


            gson.fromJson(
                json,
                type
            )

        }

    }



    suspend fun removeWrongAnswer(
        context: Context,
        questionId: Int
    ) {

        context.dataStore.edit { prefs ->


            val current =
                prefs[WRONG_QUESTIONS]
                    ?: emptySet()


            prefs[WRONG_QUESTIONS] =
                current - questionId.toString()


        }

    }




    fun getPracticeLastTime(
        context: Context
    ): Flow<Long?> {

        return context.dataStore.data.map { prefs ->

            prefs[PRACTICE_TIME]

        }

    }


}
