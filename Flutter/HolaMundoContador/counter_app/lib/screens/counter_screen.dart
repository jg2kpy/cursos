import 'package:flutter/material.dart';

class CounterScreen extends StatefulWidget {
  const CounterScreen({super.key});

  @override
  State<CounterScreen> createState() => _CounterScreenState();
}

class _CounterScreenState extends State<CounterScreen> {
  int contador = 69;

  void increase() {
    contador++;
    setState(() {});
  }

  void descrease() {
    contador--;
    setState(() {});
  }

  void setNumber(int number) {
    contador = number;
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    const fontSize30 = TextStyle(fontSize: 30);

    return Scaffold(
        appBar: AppBar(
          title: const Text('CounterScreen'),
          elevation: 10,
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              const Text('Número de Clicks', style: fontSize30),
              Text('$contador', style: fontSize30),
            ],
          ),
        ),
        floatingActionButton: CustomFloatinActions(
            increaseFn: increase,
            descreaseFn: descrease,
            setNumberFn: setNumber),
        floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat);
  }
}

class CustomFloatinActions extends StatelessWidget {
  final Function increaseFn;
  final Function descreaseFn;
  final Function setNumberFn;

  const CustomFloatinActions({
    Key? key,
    required this.increaseFn,
    required this.descreaseFn,
    required this.setNumberFn,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        FloatingActionButton(
            child: const Icon(Icons.exposure_plus_1_outlined),
            onPressed: () => increaseFn()),
        FloatingActionButton(
            child: const Icon(Icons.exposure_zero),
            onPressed: () => setNumberFn(0)),
        FloatingActionButton(
            child: const Icon(Icons.exposure_minus_1_outlined),
            onPressed: () => descreaseFn())
      ],
    );
  }
}


//() => setState(() => contador++))