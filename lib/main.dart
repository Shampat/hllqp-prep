import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'providers/quiz_provider.dart';
import 'providers/theme_provider.dart';
import 'services/billing_service.dart';
import 'services/premium_service.dart';
import 'services/purchase_verification_service.dart';
import 'screens/home_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await PremiumService.init();

  if (PurchaseVerificationService.isConfigured) {
    BillingService.instance.setVerifier(PurchaseVerificationService.verify);
  }

  await BillingService.instance.init();
  runApp(const HLLQPApp());
}

class HLLQPApp extends StatelessWidget {
  const HLLQPApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => QuizProvider()),
        ChangeNotifierProvider(create: (_) => ThemeProvider()),
        ChangeNotifierProvider.value(value: PremiumService.instance),
      ],
      child: Consumer<ThemeProvider>(
        builder: (context, themeProv, _) {
          return MaterialApp(
            title: 'HLLQP Prep - Canada',
            debugShowCheckedModeBanner: false,
            theme: themeProv.lightTheme,
            darkTheme: themeProv.darkTheme,
            themeMode: themeProv.isDark ? ThemeMode.dark : ThemeMode.light,
            home: const HomeScreen(),
          );
        },
      ),
    );
  }
}
