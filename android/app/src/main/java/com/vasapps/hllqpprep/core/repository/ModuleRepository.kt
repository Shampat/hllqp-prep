package com.vasapps.hllqpprep.core.repository

import com.vasapps.hllqpprep.core.model.ExamModule


object ModuleRepository {


    fun getModules(): List<ExamModule> {


        return listOf(

            ExamModule(
                id = "life",
                name = "Life Insurance",
                description = "Life insurance concepts, policies and applications"
            ),


            ExamModule(
                id = "accident",
                name = "Accident & Sickness",
                description = "Health insurance products and regulations"
            ),


            ExamModule(
                id = "seg",
                name = "Segregated Funds & Annuities",
                description = "Investment products and retirement planning"
            ),


            ExamModule(
                id = "ethics",
                name = "Ethics & Professional Practice",
                description = "Professional conduct and compliance"
            )

        )

    }

}
