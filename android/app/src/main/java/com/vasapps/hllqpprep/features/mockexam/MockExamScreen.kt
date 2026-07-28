package com.vasapps.hllqpprep.features.mockexam

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import com.vasapps.hllqpprep.core.ads.BannerScaffold
import com.vasapps.hllqpprep.core.repository.QuestionRepository

@Composable
fun MockExamScreen(onStartExam: () -> Unit) {
    val context = LocalContext.current
    val totalQuestions = QuestionRepository.getAllQuestions(context).size
    BannerScaffold {
        Column(modifier = Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(20.dp).padding(bottom = 20.dp), verticalArrangement = Arrangement.spacedBy(16.dp)) {
            Text("HLLQP Mock Exam", style = MaterialTheme.typography.headlineMedium)
            Text("Test your readiness under real exam conditions.", style = MaterialTheme.typography.bodyLarge)

            Card(modifier = Modifier.fillMaxWidth(), colors = CardDefaults.cardColors(containerColor = Color(0xFFE8F5E9))) {
                Column(modifier = Modifier.padding(20.dp), verticalArrangement = Arrangement.spacedBy(6.dp)) {
                    Text("QUESTION BANK", style = MaterialTheme.typography.labelLarge)
                    Text("$totalQuestions+", style = MaterialTheme.typography.headlineLarge)
                    Text("Available Questions across 9 modules", style = MaterialTheme.typography.bodyMedium)
                }
            }

            Card(modifier = Modifier.fillMaxWidth(), colors = CardDefaults.cardColors(containerColor = Color(0xFFFFF3E0))) {
                Column(modifier = Modifier.padding(20.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                    Text("EXAM FORMAT", style = MaterialTheme.typography.labelLarge)
                    Text("✓ 100 Random Questions", style = MaterialTheme.typography.bodyMedium)
                    Text("✓ Covers all modules (Life, Accident, Ethics, Tax, etc.)", style = MaterialTheme.typography.bodyMedium)
                    Text("✓ 60% to Pass (Real HLLQP standard)", style = MaterialTheme.typography.bodyMedium)
                    Text("✓ Instant explanations after exam", style = MaterialTheme.typography.bodyMedium)
                }
            }

            Card(modifier = Modifier.fillMaxWidth(), colors = CardDefaults.cardColors(containerColor = Color(0xFFE3F2FD))) {
                Column(modifier = Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(4.dp)) {
                    Text("💡 TIP", style = MaterialTheme.typography.labelLarge)
                    Text("Aim for 80%+ in practice before taking mock. Review mistakes after each attempt.", style = MaterialTheme.typography.bodySmall)
                }
            }

            Button(modifier = Modifier.fillMaxWidth().height(52.dp), onClick = onStartExam) { Text("Start Mock Exam - 100 Qs") }
        }
    }
}
