package com.vasapps.hllqpprep.core.repository

import com.vasapps.hllqpprep.core.model.Question
import com.vasapps.hllqpprep.core.repository.scenarios.EthicsQuestions
import com.vasapps.hllqpprep.core.repository.scenarios.SegregatedFundQuestions
import com.vasapps.hllqpprep.core.repository.scenarios.AnnuityQuestions
import com.vasapps.hllqpprep.core.repository.scenarios.LifeQuestions
import com.vasapps.hllqpprep.core.repository.scenarios.AccidentQuestions

object ScenarioQuestionRepository {

    fun getScenarioQuestions(
        moduleId: String
    ): List<Question> {

        return when(moduleId) {

            "ethics" -> EthicsQuestions.questions

            "segregated" -> SegregatedFundQuestions.questions

            "annuities" -> AnnuityQuestions.questions

            "life" -> LifeQuestions.questions

            "accident" -> AccidentQuestions.questions

            else -> emptyList()
        }
    }
}
