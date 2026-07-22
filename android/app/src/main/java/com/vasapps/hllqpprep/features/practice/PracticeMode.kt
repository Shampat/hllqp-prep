package com.vasapps.hllqpprep.features.practice

import com.vasapps.hllqpprep.core.model.Question

sealed class PracticeMode {

    data class Module(
        val moduleId: String
    ) : PracticeMode()


    data class Scenario(
        val moduleId: String
    ) : PracticeMode()


    data class MockExam(
        val questions: List<Question>
    ) : PracticeMode()

}
