import 'dart:convert';
import 'package:http/http.dart' as http;

import 'package:flutter_dotenv/flutter_dotenv.dart';

import 'package:api_rest/models/Gif.dart';

String url = '';

void getEnv() async {
  await dotenv.load(fileName: ".env");
  url = dotenv.env['GIPHY_URL'] ?? 'Not URL';
}

Future<List<Gif>> getGifs() async {
  List<Gif> retornoGifs = [];

  final response = await http.get(Uri.parse(url));
  if (response.statusCode == 200) {
    String body = utf8.decode(response.bodyBytes);
    final jsonData = jsonDecode(body);

    for (var item in jsonData["data"]) {
      retornoGifs.add(Gif(item["title"], item["images"]["downsized"]["url"]));
    }
  } else {
    throw Exception("Fallo en la conexión");
  }
  //print(retornoGifs);
  return retornoGifs;
}
