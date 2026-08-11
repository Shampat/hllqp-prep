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
  Question get currentQuestion => _questions.isEmpty? throw Exception("No questions") : _questions[_currentIndex];
  int get totalQuestions => _questions.length;
  bool get isLastQuestion => _questions.isEmpty? true : _currentIndex == _questions.length - 1;
  double get progress => _questions.isEmpty? 0 : (_currentIndex + 1) / _questions.length;

  // NEEDED FOR MOCK EXAM
  void setCustomQuestions(List<Question> qs, ModuleInfo module){
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
    if(_currentModule==null) return;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setInt('${_currentModule!.id}_index', _currentIndex);
    await prefs.setString('${_currentModule!.id}_answers', json.encode(_userAnswers));
    await prefs.setInt('${_currentModule!.id}_score', _score);
  }

  Future<void> loadModule(ModuleInfo module, {bool resume=true}) async {
    _isLoading = true;
    _currentModule = module;
    notifyListeners();
    try {
      final String data = await rootBundle.loadString(module.assetFile);
      final List<dynamic> jsonList = json.decode(data);
      _questions = jsonList.map((e) => Question.fromJson(e)).toList();
      _questions.shuffle();

      for(int i=1;i<_questions.length;i++){
        if(_questions[i].question.toLowerCase().trim()==_questions[i-1].question.toLowerCase().trim()){
          int swap=-1;
          for(int j=i+1;j<_questions.length;j++){
            if(_questions[j].question.toLowerCase().trim()!=_questions[i-1].question.toLowerCase().trim()){
              swap=j;break;
            }
          }
          if(swap!=-1){
            var tmp=_questions[i];
            _questions[i]=_questions[swap];
            _questions[swap]=tmp;
          }
        }
      }

      _currentIndex = 0;
      _score = 0;
      _userAnswers = List.filled(_questions.length, -1);
      _selectedAnswer = null;
      _showExplanation = false;

      if(resume){
        final prefs = await SharedPreferences.getInstance();
        int? savedIdx = prefs.getInt('${module.id}_index');
        String? savedAns = prefs.getString('${module.id}_answers');
        int? savedScore = prefs.getInt('${module.id}_score');
        if(savedIdx!=null && savedAns!=null && savedIdx < _questions.length){
          _currentIndex = savedIdx;
          _userAnswers = List<int>.from(json.decode(savedAns));
          _score = savedScore?? 0;
          _selectedAnswer = _userAnswers[_currentIndex]!=-1? _userAnswers[_currentIndex] : null;
          _showExplanation = _userAnswers[_currentIndex]!=-1;
        }
      }

    } catch (e) {
      debugPrint('Error loading ${module.id}: $e');
    }
    _isLoading = false;
    notifyListeners();
  }

  void selectAnswer(int index) {
    int prev = _userAnswers[_currentIndex];
    if(prev!=-1 && prev==currentQuestion.correctAnswer){
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
      _selectedAnswer = _userAnswers[_currentIndex]!=-1? _userAnswers[_currentIndex] : null;
      _showExplanation = _userAnswers[_currentIndex]!=-1;
      saveProgress();
      notifyListeners();
    }
  }

  void previousQuestion() {
    if (_currentIndex > 0) {
      _currentIndex--;
      _selectedAnswer = _userAnswers[_currentIndex]!=-1? _userAnswers[_currentIndex] : null;
      _showExplanation = _userAnswers[_currentIndex]!=-1;
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
    if(_currentModule!=null){
      final prefs = await SharedPreferences.getInstance();
      await prefs.remove('${_currentModule!.id}_index');
      await prefs.remove('${_currentModule!.id}_answers');
      await prefs.remove('${_currentModule!.id}_score');
    }
    notifyListeners();
  }
}
