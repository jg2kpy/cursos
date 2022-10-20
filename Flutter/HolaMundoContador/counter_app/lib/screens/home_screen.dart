import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget{

  const HomeScreen({super.key});
  
  @override
  Widget build(BuildContext context) {

    const fontSize30 = TextStyle(fontSize: 30);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Counter-Strike'),
        elevation: 10,
      ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: const <Widget>[
              Text('Número de Clikcs', style: fontSize30),
              Text('10', style: fontSize30),
            ],
          ),
        ),
        floatingActionButton: FloatingActionButton(
          child: const Text('+', style: fontSize30),
          onPressed: () => print('holaaa'),
        ),
    );
  }
  
}
