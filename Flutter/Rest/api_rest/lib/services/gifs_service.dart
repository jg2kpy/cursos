import 'dart:convert';
import 'package:http/http.dart' as http;

import 'package:flutter_dotenv/flutter_dotenv.dart';

import 'package:api_rest/models/Gif.dart';

String url = '';
String key = '';

Future getEnv() async {
  await dotenv.load(fileName: ".env");
  url = dotenv.env['API_URL'] ?? 'Not URL';
  key = dotenv.env['API_KEY'] ?? 'Not KEY';
}

Future<List<Gif>> getGifs() async {
  List<Gif> retornoGifs = [];

  Uri uri = Uri.http(url, "/v1/gifs/trending", {
    "api_key": key,
    "limit": "25",
    "rating": "g",
  });

  //print(uri);

  final response = await http.get(uri);
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

Future<List<Gif>> getGifsSearch(String search) async {
  if(search==""){
    return getGifs();
  }

  List<Gif> retornoGifs = [];

  Uri uri = Uri.http(url, "/v1/gifs/search", {
    "api_key": key,
    "q": search,
    "limit": "25",
    "rating": "g",
  });

  //print(uri);

  final response = await http.get(uri);
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
