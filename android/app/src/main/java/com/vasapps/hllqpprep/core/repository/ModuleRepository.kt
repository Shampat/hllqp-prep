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
                id = "segregated",
                name = "Segregated Funds",
                description = "Segregated funds concepts and regulations"
            ),


            ExamModule(
                id = "annuities",
                name = "Annuities",
                description = "Annuity products and retirement planning"
            ),


            ExamModule(
                id = "ethics",
                name = "Ethics & Professional Practice",
                description = "Professional conduct and compliance"
            )

        )

    }

}
