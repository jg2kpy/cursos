import 'package:flutter/material.dart';

class Listview1Screen extends StatelessWidget {
  const Listview1Screen({Key? key}) : super(key: key);

  final options = const ['Megaman', 'Metal Gear'];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Listview Tipo 1"),
      ),
      body: ListView(
        children: [

          ...options
              .map((game) => ListTile(
                    title: Text(game),
                    trailing: const Icon(Icons.arrow_forward_ios),
                  ))
              .toList(),
              
          const Divider(),

        ],
      ),
    );
  }
}
