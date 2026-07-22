package com.vasapps.hllqpprep.features.module

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.foundation.clickable
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import com.vasapps.hllqpprep.core.repository.ModuleRepository


private fun moduleColor(id: String): Color {
    return when (id) {
        "life" -> Color(0xFFE3F2FD)
        "accident" -> Color(0xFFE0F7FA)
        "segregated" -> Color(0xFFF3E5F5)
        "annuities" -> Color(0xFFFFF3E0)
        "ethics" -> Color(0xFFFFEBEE)
        else -> Color.White
    }
}



@Composable
fun ModuleScreen(
    onBack: () -> Unit,
    onModuleSelected: (String) -> Unit
) {


    val modules =
        ModuleRepository.getModules()



    Column(

        modifier =
            Modifier
                .fillMaxSize()
                .padding(24.dp)
                .verticalScroll(
                    rememberScrollState()
                ),

        verticalArrangement =
            Arrangement.spacedBy(16.dp)

    ) {



        Row(
            modifier = Modifier.clickable {
                onBack()
            },
            horizontalArrangement = Arrangement.spacedBy(4.dp)
        ) {

            Icon(
                imageVector = Icons.Default.ArrowBack,
                contentDescription = "Back"
            )

            Text(
                text = "Choose Your Study Module",
                style = MaterialTheme.typography.titleMedium
            )

        }





        Text(

            text =
                "Practice questions and review concepts by HLLQP section.",

            style =
                MaterialTheme.typography.bodyLarge

        )




        modules.forEach { module ->



            Card(

                modifier =
                    Modifier.fillMaxWidth(),

                onClick = {

                    onModuleSelected(module.id)

                },

                colors =
                    CardDefaults.cardColors(
                        containerColor = moduleColor(module.id)
                    )

            ) {



                Column(

                    modifier =
                        Modifier.padding(20.dp),

                    verticalArrangement =
                        Arrangement.spacedBy(8.dp)

                ) {



                    Text(

                        text =
                            module.name,

                        style =
                            MaterialTheme.typography.titleLarge

                    )



                    Text(

                        text =
                            module.description,

                        style =
                            MaterialTheme.typography.bodyMedium

                    )



                }


            }


        }


    }


}
