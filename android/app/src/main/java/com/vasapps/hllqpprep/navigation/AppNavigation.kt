package com.vasapps.hllqpprep.navigation

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.MenuBook
import androidx.compose.material.icons.filled.Quiz
import androidx.compose.material.icons.filled.Style
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.foundation.layout.padding
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext

import com.vasapps.hllqpprep.features.home.HomeScreen
import com.vasapps.hllqpprep.features.practiceSetup.PracticeSetupScreen
import com.vasapps.hllqpprep.features.module.ModuleScreen
import com.vasapps.hllqpprep.features.practice.PracticeScreen
import com.vasapps.hllqpprep.features.practice.PracticeMode
import com.vasapps.hllqpprep.features.mockexam.MockExamScreen
import com.vasapps.hllqpprep.features.flashcards.FlashcardsScreen
import com.vasapps.hllqpprep.features.review.ReviewWrongAnswersScreen
import com.vasapps.hllqpprep.features.history.ExamHistoryScreen
import com.vasapps.hllqpprep.core.repository.QuestionRepository


@Composable
fun AppNavigation() {

    val context = LocalContext.current

    var selectedTab by remember {
        mutableStateOf(0)
    }


    var practiceFlow by remember {
        mutableStateOf("none")
    }


    var showReview by remember {
        mutableStateOf(false)
    }


    var showHistory by remember {
        mutableStateOf(false)
    }


    var selectedModule by remember {
        mutableStateOf("")
    }


    var mockQuestions by remember {
        mutableStateOf(emptyList<com.vasapps.hllqpprep.core.model.Question>())
    }


    Scaffold(

        bottomBar = {

            NavigationBar {

                NavigationBarItem(
                    selected = selectedTab == 0,
                    onClick = {
                        selectedTab = 0
                        practiceFlow = "none"
                    },
                    icon = {
                        Icon(Icons.Default.Home, "Home")
                    },
                    label = {
                        Text("Home")
                    }
                )


                NavigationBarItem(
                    selected = selectedTab == 1,
                    onClick = {
                        selectedTab = 1
                    },
                    icon = {
                        Icon(Icons.Default.MenuBook, "Practice")
                    },
                    label = {
                        Text("Practice")
                    }
                )


                NavigationBarItem(
                    selected = selectedTab == 2,
                    onClick = {
                        selectedTab = 2
                    },
                    icon = {
                        Icon(Icons.Default.Quiz, "Mock")
                    },
                    label = {
                        Text("Mock")
                    }
                )


                NavigationBarItem(
                    selected = selectedTab == 3,
                    onClick = {
                        selectedTab = 3
                    },
                    icon = {
                        Icon(Icons.Default.Style, "Cards")
                    },
                    label = {
                        Text("Cards")
                    }
                )

            }

        }

    ) { padding ->


        Surface(
            modifier = Modifier.padding(padding)
        ) {


            when(selectedTab) {


                0 -> {


                    if (showReview) {


                        ReviewWrongAnswersScreen(

                            onBack = {

                                showReview = false

                            }

                        )


                    } else if (showHistory) {


                        ExamHistoryScreen(

                            onBack = {

                                showHistory = false

                            }

                        )


                    } else {


                    HomeScreen(
                        onPracticeClick = {
                            selectedTab = 1
                        },
                        onMockExamClick = {
                            selectedTab = 2
                        },
                        onFlashcardsClick = {
                            selectedTab = 3
                        },

                        onReviewClick = {

                            showReview = true

                        },


                        onHistoryClick = {

                            showHistory = true

                        }

                    )


                    }


                }



                1 -> {


                    when(practiceFlow) {


                        "none" -> {

                            PracticeSetupScreen(

                                onBack = {
                                    selectedTab = 0
                                },

                                onStartPractice = {

                                    practiceFlow = "module"

                                }

                            )

                        }


                        "module" -> {

                            ModuleScreen(

                                onBack = {
                                    practiceFlow = "none"
                                },

                                onModuleSelected = {

                                    selectedModule = it
                                    practiceFlow = "practice"

                                }

                            )

                        }


                        "practice" -> {

                            PracticeScreen(
                                mode = PracticeMode.Module(selectedModule),

                                onBack = {
                                    practiceFlow = "module"
                                }
                            )

                        }

                    }


                }



                2 -> {

                    if (mockQuestions.isEmpty()) {

                        MockExamScreen(
                            onStartExam = {

                                mockQuestions =
                                    QuestionRepository
                                        .getAllQuestions(
                                            context
                                        )
                                        .shuffled()
                                        .take(10)

                            }
                        )

                    } else {

                        PracticeScreen(
                            mode = PracticeMode.MockExam(mockQuestions),

                            onBack = {
                                mockQuestions = emptyList()
                            }
                        )

                    }

                }



                3 -> {

                    FlashcardsScreen()

                }


            }

        }

    }

}
