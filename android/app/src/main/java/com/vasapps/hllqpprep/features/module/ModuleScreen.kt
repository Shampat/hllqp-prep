package com.vasapps.hllqpprep.features.module

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.vasapps.hllqpprep.core.repository.ModuleRepository


@Composable
fun ModuleScreen(
    onBack: () -> Unit,
    onModuleSelected: (String) -> Unit
) {


    val modules = ModuleRepository.getModules()


    Column(

        modifier = Modifier
            .fillMaxSize()
            .padding(24.dp)
            .verticalScroll(rememberScrollState()),

        verticalArrangement = Arrangement.spacedBy(16.dp)

    ) {


        Button(
            onClick = onBack
        ) {

            Text("Back")

        }


        Text(
            text = "Select HLLQP Module",
            style = MaterialTheme.typography.headlineMedium
        )


        modules.forEach { module ->


            Card(

                modifier = Modifier.fillMaxWidth(),

                onClick = {

                    onModuleSelected(module.id)

                }

            ) {


                Column(
                    modifier = Modifier.padding(20.dp)
                ) {


                    Text(
                        text = module.name,
                        style = MaterialTheme.typography.titleMedium
                    )


                    Text(
                        text = module.description
                    )


                }


            }


        }


    }


}
