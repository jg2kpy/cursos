import 'package:flutter/material.dart';

class Listview2Screen extends StatelessWidget {
  const Listview2Screen({Key? key}) : super(key: key);

  final options = const [
    'Megaman',
    'Metal Gear',
    'Final Fantasy',
    'Come Closer'
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Listview Tipo 2"),
        backgroundColor: Colors.indigo,
      ),
      body: ListView.separated(

          itemBuilder: (context, index) => ListTile(
                title: Text(options[index]),
                trailing:
                    const Icon(Icons.arrow_forward_ios, color: Colors.indigo),
                onTap: () {
                  //print(options[index]);
                },
              ),
          separatorBuilder: (_, __) => const Divider(),
          itemCount: options.length),
          
    );
  }
}
