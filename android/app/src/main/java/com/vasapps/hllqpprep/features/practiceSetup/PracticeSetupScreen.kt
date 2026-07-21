package com.vasapps.hllqpprep.features.practiceSetup

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp


@Composable
fun PracticeSetupScreen(
    onBack: () -> Unit,
    onStartPractice: () -> Unit
) {


    Column(

        modifier =
            Modifier
                .fillMaxSize()
                .padding(24.dp),

        verticalArrangement =
            Arrangement.spacedBy(20.dp)

    ) {



        Button(
            onClick = onBack
        ) {

            Text("Back")

        }




        Text(

            text =
                "Practice Setup",

            style =
                MaterialTheme.typography.headlineMedium

        )



        Text(

            text =
                "Prepare by module with focused practice questions.",

            style =
                MaterialTheme.typography.bodyLarge

        )




        Card(

            modifier =
                Modifier.fillMaxWidth()

        ) {



            Column(

                modifier =
                    Modifier.padding(20.dp),

                verticalArrangement =
                    Arrangement.spacedBy(10.dp)

            ) {



                Text(

                    text =
                        "Practice Mode",

                    style =
                        MaterialTheme.typography.titleMedium

                )



                Text(
                    "• Instant explanations"
                )


                Text(
                    "• Track your progress"
                )


                Text(
                    "• Review difficult questions"
                )


            }


        }





        Button(

            onClick =
                onStartPractice,

            modifier =
                Modifier.fillMaxWidth()

        ) {


            Text(
                "Start Practice"
            )


        }


    }

}
