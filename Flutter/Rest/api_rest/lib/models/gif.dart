class Gif {
  String name = '';
  String url = '';

  Gif(this.name, this.url);

  @override
  String toString() {
    return "Nombre:$name-URL:$url";
  }
}
