package com.vasapps.hllqpprep.features.home

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.MenuBook
import androidx.compose.material.icons.filled.Quiz
import androidx.compose.material.icons.filled.Style
import androidx.compose.material.icons.filled.Warning
import androidx.compose.material.icons.filled.History
import androidx.compose.material.icons.filled.TrendingUp
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.setValue
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import kotlinx.coroutines.launch
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Button
import com.vasapps.hllqpprep.core.utils.ProgressManager
import com.vasapps.hllqpprep.ui.theme.InsuranceBlue
import com.vasapps.hllqpprep.ui.theme.InsuranceBlueDark
import com.vasapps.hllqpprep.ui.theme.TealProgress


@Composable
fun HomeScreen(
    onPracticeClick: () -> Unit,
    onMockExamClick: () -> Unit,
    onFlashcardsClick: () -> Unit,
    onReviewClick: () -> Unit,
    onHistoryClick: () -> Unit
) {

    val context = LocalContext.current

    val progress =
        ProgressManager.getProgress(context)
            .collectAsState(initial = Pair(0, 0))


    val attempted = progress.value.first
    val correct = progress.value.second

    val accuracy =
        if (attempted > 0)
            (correct * 100) / attempted
        else
            0



    val readiness =
        when {

            accuracy >= 80 && attempted >= 100 ->
                "Ready for Exam"

            accuracy >= 70 ->
                "Good Progress"

            attempted > 0 ->
                "Keep Practicing"

            else ->
                "Start Your Preparation"

        }



    val scope = rememberCoroutineScope()


    var showResetDialog by remember {
        mutableStateOf(false)
    }


    if (showResetDialog) {

        AlertDialog(

            onDismissRequest = {
                showResetDialog = false
            },

            title = {
                Text("Reset Progress?")
            },

            text = {
                Text(
                    "This will clear your practice progress, score and mistakes."
                )
            },

            confirmButton = {

                Button(
                    onClick = {

                        scope.launch {

                            ProgressManager.clearProgress(context)

                        }

                        showResetDialog = false

                    }
                ) {

                    Text("Reset")

                }

            },

            dismissButton = {

                Button(
                    onClick = {
                        showResetDialog = false
                    }
                ) {

                    Text("Cancel")

                }

            }

        )

    }


    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp)
            .verticalScroll(rememberScrollState()),

        verticalArrangement = Arrangement.spacedBy(18.dp)
    ) {


        Text(
            text = "HLLQP Prep Canada",
            style = MaterialTheme.typography.headlineMedium,
            color = InsuranceBlueDark
        )


        Text(
            text = "Your path to Canadian insurance licensing success.",
            style = MaterialTheme.typography.bodyLarge
        )



        Card(
            modifier = Modifier.fillMaxWidth(),
            colors = CardDefaults.cardColors(
                containerColor = Color(0xFFE3F2FD)
            )
        ) {

            Column(
                modifier = Modifier.padding(20.dp),
                verticalArrangement = Arrangement.spacedBy(10.dp)
            ) {


                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween
                ) {

                    Row(
                        horizontalArrangement = Arrangement.spacedBy(6.dp)
                    ) {

                        Text(
                            text = "YOUR PROGRESS",
                            style = MaterialTheme.typography.labelLarge
                        )

                        Icon(
                            imageVector = Icons.Default.TrendingUp,
                            contentDescription = null,
                            tint = TealProgress
                        )

                    }


                    Text(
                        text = "RESET",
                        color = InsuranceBlue,
                        modifier = Modifier.clickable {
                            showResetDialog = true
                        }
                    )

                }


                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween
                ) {

                    Text(
                        text = "$attempted Questions",
                        style = MaterialTheme.typography.titleMedium
                    )


                    Text(
                        text = "$accuracy% Accuracy",
                        style = MaterialTheme.typography.titleMedium
                    )

                }

            }

        }



        Text(
            text = "📚 STUDY TOOLS",
            style = MaterialTheme.typography.labelLarge
        )



        StudyCard(
            icon = Icons.Default.MenuBook,
            title = "Practice Questions",
            description = "Practice by module with instant explanations.",
            iconColor = InsuranceBlue,
            onClick = onPracticeClick
        )



        StudyCard(
            icon = Icons.Default.Quiz,
            title = "Mock Exam",
            description = "Simulate the HLLQP exam experience.",
            iconColor = TealProgress,
            onClick = onMockExamClick
        )



        StudyCard(
            icon = Icons.Default.Style,
            title = "Flashcards",
            description = "Review important concepts quickly.",
            iconColor = InsuranceBlueDark,
            onClick = onFlashcardsClick
        )


        StudyCard(
            icon = Icons.Default.Warning,
            title = "Review Mistakes",
            description = "Focus on questions you answered incorrectly.",
            iconColor = Color(0xFFC62828),
            onClick = onReviewClick
        )

    }

}



@Composable
private fun StudyCard(
    icon: androidx.compose.ui.graphics.vector.ImageVector,
    title: String,
    description: String,
    iconColor: Color,
    onClick: () -> Unit
) {

    Card(
        modifier = Modifier.fillMaxWidth(),
        onClick = onClick,
        colors = CardDefaults.cardColors(
            containerColor = iconColor.copy(alpha = 0.08f)
        )
    ) {

        Row(
            modifier = Modifier.padding(20.dp),
            horizontalArrangement = Arrangement.spacedBy(16.dp)
        ) {

            Icon(
                imageVector = icon,
                contentDescription = null,
                tint = iconColor,
                modifier = Modifier.size(32.dp)
            )

            Column(
                verticalArrangement = Arrangement.spacedBy(4.dp)
            ) {

                Text(
                    text = title,
                    style = MaterialTheme.typography.titleMedium
                )

                Text(
                    text = description,
                    style = MaterialTheme.typography.bodyMedium
                )

            }

        }

    }

}
