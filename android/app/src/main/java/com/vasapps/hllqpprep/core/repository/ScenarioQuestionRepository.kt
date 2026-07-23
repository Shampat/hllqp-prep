package com.vasapps.hllqpprep.core.repository

import com.vasapps.hllqpprep.core.model.Question
import com.vasapps.hllqpprep.core.repository.scenarios.EthicsQuestions
import com.vasapps.hllqpprep.core.repository.scenarios.SegregatedFundQuestions
import com.vasapps.hllqpprep.core.repository.scenarios.AnnuityQuestions
import com.vasapps.hllqpprep.core.repository.scenarios.LifeQuestions
import com.vasapps.hllqpprep.core.repository.scenarios.AccidentQuestions

import com.vasapps.hllqpprep.core.repository.scenarios.DisabilityQuestions
import com.vasapps.hllqpprep.core.repository.scenarios.CriticalIllnessQuestions
import com.vasapps.hllqpprep.core.repository.scenarios.TaxationQuestions
import com.vasapps.hllqpprep.core.repository.scenarios.EstatePlanningQuestions

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

            "disability" -> DisabilityQuestions.questions

            "critical_illness" -> CriticalIllnessQuestions.questions

            "taxation" -> TaxationQuestions.questions

            "estate" -> EstatePlanningQuestions.questions

            else -> emptyList()
        }
    }
}
