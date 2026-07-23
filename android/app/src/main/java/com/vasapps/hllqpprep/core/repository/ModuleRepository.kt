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
            ),

            ExamModule(
                id = "disability",
                name = "Disability Insurance",
                description = "Disability income protection concepts and applications"
            ),

            ExamModule(
                id = "critical_illness",
                name = "Critical Illness Insurance",
                description = "Critical illness coverage concepts and policy features"
            ),

            ExamModule(
                id = "taxation",
                name = "Taxation",
                description = "Tax concepts, registered plans and financial planning"
            ),

            ExamModule(
                id = "estate",
                name = "Estate Planning",
                description = "Estate planning concepts, beneficiaries and succession"
            )

        )

    }

}
