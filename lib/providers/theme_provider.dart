import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class ThemeProvider extends ChangeNotifier {
  bool _isDark = false;
  bool get isDark => _isDark;

  ThemeProvider() { _load(); }

  Future<void> _load() async {
    final prefs = await SharedPreferences.getInstance();
    _isDark = prefs.getBool('isDark')?? false;
    notifyListeners();
  }

  Future<void> toggle() async {
    _isDark =!_isDark;
    notifyListeners();
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool('isDark', _isDark);
  }

  ThemeData get lightTheme => ThemeData(
    useMaterial3: false, // IMPORTANT: no M3 yellow/red overflow
    brightness: Brightness.light,
    primaryColor: Colors.indigo,
    scaffoldBackgroundColor: Colors.white,
    appBarTheme: const AppBarTheme(backgroundColor: Colors.indigo, foregroundColor: Colors.white, elevation: 0),
    cardTheme: const CardThemeData(color: Colors.white, elevation: 2),
    elevatedButtonTheme: ElevatedButtonThemeData(style: ElevatedButton.styleFrom(backgroundColor: Colors.indigo, foregroundColor: Colors.white)),
  );

  ThemeData get darkTheme => ThemeData(
    useMaterial3: false,
    brightness: Brightness.dark,
    primaryColor: Colors.indigo,
    scaffoldBackgroundColor: const Color(0xFF121212),
    appBarTheme: const AppBarTheme(backgroundColor: Color(0xFF1A1A2E), foregroundColor: Colors.white, elevation: 0),
    cardTheme: const CardThemeData(color: Color(0xFF1E1E1E), elevation: 2),
    elevatedButtonTheme: ElevatedButtonThemeData(style: ElevatedButton.styleFrom(backgroundColor: const Color(0xFF3949AB), foregroundColor: Colors.white)),
  );
}
