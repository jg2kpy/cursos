import 'animal.dart';

class Duck extends Animal {
  
  @override
  String toString() {
    return "Soy un pato y soy de $age edad";
  }

  @override
  void makeNoise() {
    print('Quackk');
  }
}
