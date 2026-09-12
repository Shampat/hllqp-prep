import 'dart:convert';
import 'package:flutter/services.dart';
import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/question.dart';
import '../models/module.dart';

class QuizProvider extends ChangeNotifier {
  List<Question> _questions = [];
  int _currentIndex = 0;
  int _score = 0;
  int? _selectedAnswer;
  bool _showExplanation = false;
  bool _isLoading = false;
  ModuleInfo? _currentModule;
  List<int> _userAnswers = [];

  List<Question> get questions => _questions;
  int get currentIndex => _currentIndex;
  int get score => _score;
  int? get selectedAnswer => _selectedAnswer;
  bool get showExplanation => _showExplanation;
  bool get isLoading => _isLoading;
  ModuleInfo? get currentModule => _currentModule;
  Question get currentQuestion => _questions.isEmpty
      ? throw Exception("No questions")
      : _questions[_currentIndex];
  int get totalQuestions => _questions.length;
  bool get isLastQuestion =>
      _questions.isEmpty ? true : _currentIndex == _questions.length - 1;
  double get progress =>
      _questions.isEmpty ? 0 : (_currentIndex + 1) / _questions.length;

  // NEEDED FOR MOCK EXAM
  void setCustomQuestions(List<Question> qs, ModuleInfo module) {
    _questions = qs;
    _currentModule = module;
    _currentIndex = 0;
    _score = 0;
    _selectedAnswer = null;
    _showExplanation = false;
    _userAnswers = List.filled(_questions.length, -1);
    _isLoading = false;
    notifyListeners();
  }

  Future<void> saveProgress() async {
    if (_currentModule == null) return;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setInt('${_currentModule!.id}_index', _currentIndex);
    await prefs.setString(
      '${_currentModule!.id}_answers',
      json.encode(_userAnswers),
    );
    await prefs.setInt('${_currentModule!.id}_score', _score);
    await prefs.setString(
      '${_currentModule!.id}_order',
      json.encode(_questions.map((q) => q.id.toString()).toList()),
    );
  }

  bool _isValidAnswerList(dynamic decoded, int questionCount) {
    if (decoded is! List || decoded.length != questionCount) return false;
    for (final value in decoded) {
      if (value is! int || value < -1 || value > 3) return false;
    }
    return true;
  }

  List<Question>? _restoreSavedOrder(
    List<Question> questions,
    String? savedOrder,
  ) {
    if (savedOrder == null) return null;
    try {
      final decoded = json.decode(savedOrder);
      if (decoded is! List || decoded.length != questions.length) return null;

      final byId = <String, Question>{};
      for (final question in questions) {
        final key = question.id.toString();
        if (byId.containsKey(key)) return null;
        byId[key] = question;
      }

      final restored = <Question>[];
      final seen = <String>{};
      for (final value in decoded) {
        final key = value.toString();
        final question = byId[key];
        if (question == null || !seen.add(key)) return null;
        restored.add(question);
      }
      return restored.length == questions.length ? restored : null;
    } catch (_) {
      return null;
    }
  }

  Future<void> loadModule(ModuleInfo module, {bool resume = true}) async {
    _isLoading = true;
    _currentModule = module;
    notifyListeners();

    try {
      final String data = await rootBundle.loadString(module.assetFile);
      final List<dynamic> jsonList = json.decode(data);
      final loadedQuestions = jsonList.map((e) => Question.fromJson(e)).toList();
      final prefs = await SharedPreferences.getInstance();

      final savedOrder = resume ? prefs.getString('${module.id}_order') : null;
      final restoredOrder = _restoreSavedOrder(loadedQuestions, savedOrder);
      final canResumeSavedAnswers = resume && restoredOrder != null;

      if (restoredOrder != null) {
        _questions = restoredOrder;
      } else {
        _questions = loadedQuestions..shuffle();
      }

      _currentIndex = 0;
      _score = 0;
      _userAnswers = List.filled(_questions.length, -1);
      _selectedAnswer = null;
      _showExplanation = false;

      // Answers are index-based, so they are restored only when the exact
      // question-id order that produced them was also restored successfully.
      // Legacy progress without a saved order is intentionally discarded.
      if (canResumeSavedAnswers) {
        final savedIdx = prefs.getInt('${module.id}_index');
        final savedAns = prefs.getString('${module.id}_answers');
        final savedScore = prefs.getInt('${module.id}_score');

        if (savedIdx != null &&
            savedIdx >= 0 &&
            savedIdx < _questions.length &&
            savedAns != null) {
          try {
            final decodedAnswers = json.decode(savedAns);
            if (_isValidAnswerList(decodedAnswers, _questions.length)) {
              _currentIndex = savedIdx;
              _userAnswers = List<int>.from(decodedAnswers);
              _score = savedScore ?? 0;
              _selectedAnswer = _userAnswers[_currentIndex] != -1
                  ? _userAnswers[_currentIndex]
                  : null;
              _showExplanation = _userAnswers[_currentIndex] != -1;
            }
          } catch (_) {
            // Ignore incompatible or corrupted saved progress.
          }
        }
      }

      // Persist the exact order used by this session so future resumes are safe.
      await prefs.setString(
        '${module.id}_order',
        json.encode(_questions.map((q) => q.id.toString()).toList()),
      );

      if (!canResumeSavedAnswers) {
        await prefs.setInt('${module.id}_index', 0);
        await prefs.setString(
          '${module.id}_answers',
          json.encode(_userAnswers),
        );
        await prefs.setInt('${module.id}_score', 0);
      }
    } catch (e) {
      debugPrint('Error loading ${module.id}: $e');
    }

    _isLoading = false;
    notifyListeners();
  }

  void selectAnswer(int index) {
    int prev = _userAnswers[_currentIndex];
    if (prev != -1 && prev == currentQuestion.correctAnswer) {
      _score--;
    }
    _selectedAnswer = index;
    _userAnswers[_currentIndex] = index;
    _showExplanation = true;
    if (index == currentQuestion.correctAnswer) _score++;
    saveProgress();
    notifyListeners();
  }

  void nextQuestion() {
    if (_currentIndex < _questions.length - 1) {
      _currentIndex++;
      _selectedAnswer = _userAnswers[_currentIndex] != -1
          ? _userAnswers[_currentIndex]
          : null;
      _showExplanation = _userAnswers[_currentIndex] != -1;
      saveProgress();
      notifyListeners();
    }
  }

  void previousQuestion() {
    if (_currentIndex > 0) {
      _currentIndex--;
      _selectedAnswer = _userAnswers[_currentIndex] != -1
          ? _userAnswers[_currentIndex]
          : null;
      _showExplanation = _userAnswers[_currentIndex] != -1;
      saveProgress();
      notifyListeners();
    }
  }

  Future<void> reset() async {
    _currentIndex = 0;
    _score = 0;
    _selectedAnswer = null;
    _showExplanation = false;
    _userAnswers = List.filled(_questions.length, -1);
    if (_currentModule != null) {
      final prefs = await SharedPreferences.getInstance();
      await prefs.remove('${_currentModule!.id}_index');
      await prefs.remove('${_currentModule!.id}_answers');
      await prefs.remove('${_currentModule!.id}_score');
      await prefs.remove('${_currentModule!.id}_order');
    }
    notifyListeners();
  }
}