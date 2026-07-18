package com.vasapps.hllqpprep.core.model

data class Question(
    val id: Int,
    val moduleId: String,
    val moduleName: String,
    val topic: String,
    val difficulty: String,
    val question: String,
    val options: List<String>,
    val correctAnswer: Int,
    val explanation: String
)
