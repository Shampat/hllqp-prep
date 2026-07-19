package com.vasapps.hllqpprep.core.utils

import android.content.Context
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.intPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

private val Context.dataStore by preferencesDataStore(
    name = "user_progress"
)

object ProgressManager {

    private val TOTAL_ATTEMPTED =
        intPreferencesKey("total_attempted")

    private val TOTAL_CORRECT =
        intPreferencesKey("total_correct")


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
}
