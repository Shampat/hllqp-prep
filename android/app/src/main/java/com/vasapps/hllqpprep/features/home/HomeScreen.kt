package com.vasapps.hllqpprep.features.home

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import com.vasapps.hllqpprep.core.utils.ProgressManager
import com.vasapps.hllqpprep.ui.theme.*
import kotlinx.coroutines.launch

@Composable
fun HomeScreen(
    onPracticeClick: () -> Unit,
    onMockExamClick: () -> Unit,
    onFlashcardsClick: () -> Unit,
    onReviewClick: () -> Unit,
    onHistoryClick: () -> Unit
) {
    val context = LocalContext.current
    val progress = ProgressManager.getProgress(context).collectAsState(initial = Pair(0, 0))
    val attempted = progress.value.first
    val correct = progress.value.second
    val accuracy = if (attempted > 0) (correct * 100) / attempted else 0
    val readiness = when {
        accuracy >= 80 && attempted >= 100 -> "✅ Ready for Exam"
        accuracy >= 70 -> "Good Progress"
        attempted > 0 -> "Keep Practicing"
        else -> "Start Your Preparation"
    }
    val scope = rememberCoroutineScope()
    var showResetDialog by remember { mutableStateOf(false) }

    if (showResetDialog) {
        AlertDialog(
            onDismissRequest = { showResetDialog = false },
            title = { Text("Reset Progress?") },
            text = { Text("This will clear your practice progress, score and mistakes.") },
            confirmButton = {
                Button(onClick = {
                    scope.launch { ProgressManager.clearProgress(context) }
                    showResetDialog = false
                }) { Text("Reset") }
            },
            dismissButton = { Button(onClick = { showResetDialog = false }) { Text("Cancel") } }
        )
    }

    Column(
        modifier = Modifier.fillMaxSize().padding(20.dp).verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(18.dp)
    ) {
        Text("HLLQP Prep Canada", style = MaterialTheme.typography.headlineMedium, color = InsuranceBlueDark)
        Text("Your path to Canadian insurance licensing success.", style = MaterialTheme.typography.bodyLarge)
        Text("Status: $readiness", style = MaterialTheme.typography.titleSmall, color = TealProgress)

        Card(modifier = Modifier.fillMaxWidth(), colors = CardDefaults.cardColors(containerColor = Color(0xFFE3F2FD))) {
            Column(modifier = Modifier.padding(20.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
                    Row(horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                        Text("YOUR PROGRESS", style = MaterialTheme.typography.labelLarge)
                        Icon(Icons.Default.TrendingUp, null, tint = TealProgress)
                    }
                    Text("RESET", color = InsuranceBlue, modifier = Modifier.clickable { showResetDialog = true })
                }
                Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
                    Text("$attempted Questions", style = MaterialTheme.typography.titleMedium)
                    Text("$accuracy% Accuracy", style = MaterialTheme.typography.titleMedium)
                }
            }
        }

        Text("📚 STUDY TOOLS", style = MaterialTheme.typography.labelLarge)

        StudyCard(Icons.Default.MenuBook, "Practice Questions", "Practice by module with instant explanations.", InsuranceBlue, Color(0xFFE3F2FD), onPracticeClick)
        StudyCard(Icons.Default.Quiz, "Mock Exam", "100 Qs • Real exam simulation • 60% to pass", Color(0xFFEF6C00), Color(0xFFFFF3E0), onMockExamClick)
        StudyCard(Icons.Default.Style, "Flashcards", "Review important concepts quickly.", Color(0xFF7B1FA2), Color(0xFFF3E5F5), onFlashcardsClick)
        StudyCard(Icons.Default.Warning, "Review Mistakes", "Focus on questions you answered incorrectly.", ErrorRed, Color(0xFFFFEBEE), onReviewClick)
        StudyCard(Icons.Default.History, "Exam History", "View past mock exam results and progress.", SuccessGreen, Color(0xFFE8F5E9), onHistoryClick)
    }
}

@Composable
private fun StudyCard(icon: androidx.compose.ui.graphics.vector.ImageVector, title: String, description: String, iconColor: Color, bgColor: Color, onClick: () -> Unit) {
    Card(modifier = Modifier.fillMaxWidth(), onClick = onClick, colors = CardDefaults.cardColors(containerColor = bgColor)) {
        Row(modifier = Modifier.padding(20.dp), horizontalArrangement = Arrangement.spacedBy(16.dp)) {
            Icon(icon, null, tint = iconColor, modifier = Modifier.size(32.dp))
            Column(verticalArrangement = Arrangement.spacedBy(4.dp)) {
                Text(title, style = MaterialTheme.typography.titleMedium)
                Text(description, style = MaterialTheme.typography.bodyMedium, color = TextSecondary)
            }
        }
    }
}
