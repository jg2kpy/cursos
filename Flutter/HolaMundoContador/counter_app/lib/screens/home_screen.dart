import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget{

  const HomeScreen({super.key});
  
  @override
  Widget build(BuildContext context) {

    const fontSize30 = TextStyle(fontSize: 30);

    int contador = 69;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Counter-Strike'),
        elevation: 10,
      ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              const Text('Número de Clicks', style: fontSize30),
              Text('$contador' , style: fontSize30),
            ],
          ),
        ),
        floatingActionButton: FloatingActionButton( 
          child: const Icon(Icons.add),
          onPressed: () {
            contador++;
            //print(contador++);
          }
        ),
        floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat
    );
  }
  
}
