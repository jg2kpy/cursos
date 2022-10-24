import 'package:flutter/material.dart';

import 'package:api_rest/models/Gif.dart';
import 'package:api_rest/services/gifs_service.dart';

String url = '';

Future main() async {
  getEnv();
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  late Future<List<Gif>> _listadoGifs;

  @override
  void initState() {
    super.initState();
    _listadoGifs = getGifs();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Gifs app',
      home: Scaffold(
          appBar: AppBar(
            title: const Text('Gifs app'),
          ),
          body: FutureBuilder(
            future: _listadoGifs,
            builder: (context, snapshot) {
              if (snapshot.hasData) {
                //print(snapshot.data);
                return GridView.count(
                  crossAxisCount: 2,
                  children: _listGifs(snapshot.data),
                );
              } else if (snapshot.hasError) {
                //print(snapshot.error);
                return const Text("Error al obtener los gifs");
              }
              return const Center(
                child: CircularProgressIndicator(),
              );
            },
          )),
    );
  }

  List<Widget> _listGifs(List<Gif>? data) {
    List<Widget> gifs = [];

    for (var gif in data!) {
      gifs.add(Card(
          child: Column(
        children: [
          Expanded(
              child: Image.network(
            gif.url,
            fit: BoxFit.fill,
          )),
        ],
      )));
    }
    return gifs;
  }
}
