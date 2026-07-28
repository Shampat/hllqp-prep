package com.vasapps.hllqpprep.core.ads

import android.content.Context
import androidx.datastore.preferences.core.booleanPreferencesKey
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

private val Context.dataStore by preferencesDataStore(name = "premium_prefs")

object PremiumManager {
    private val IS_PREMIUM = booleanPreferencesKey("is_premium")
    
    fun isPremiumFlow(context: Context): Flow<Boolean> {
        return context.dataStore.data.map { prefs ->
            prefs[IS_PREMIUM] ?: false
        }
    }
    
    suspend fun setPremium(context: Context, premium: Boolean) {
        context.dataStore.edit { prefs ->
            prefs[IS_PREMIUM] = premium
        }
    }
}
