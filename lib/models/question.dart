class Question {
  final dynamic id; // allow int or String
  final String moduleId;
  final String moduleName;
  final String topic;
  final String difficulty;
  final String question;
  final List<String> options;
  final int correctAnswer;
  final String explanation;

  Question({
    required this.id,
    required this.moduleId,
    required this.moduleName,
    required this.topic,
    required this.difficulty,
    required this.question,
    required this.options,
    required this.correctAnswer,
    required this.explanation,
  });

  factory Question.fromJson(Map<String, dynamic> json) {
    return Question(
      id: json['id'] ?? 0,
      moduleId: json['moduleId']?.toString() ?? json['module']?.toString() ?? 'life',
      moduleName: json['moduleName']?.toString() ?? json['moduleId']?.toString() ?? 'Life',
      topic: json['topic']?.toString() ?? 'General',
      difficulty: json['difficulty']?.toString() ?? 'Medium',
      question: json['question']?.toString() ?? '',
      options: json['options'] != null ? List<String>.from(json['options'].map((e)=>e.toString())) : ["A","B","C","D"],
      correctAnswer: json['correctAnswer'] is int ? json['correctAnswer'] : int.tryParse(json['correctAnswer'].toString()) ?? 0,
      explanation: json['explanation']?.toString() ?? 'No explanation',
    );
  }
}
