import 'animal.dart';
import 'domestic.dart';
import 'human_age.dart';

class Cat extends Animal with Domestic implements HumanAge{

  final String name;
  Cat(this.name);

  pur() {
    print('prrrr');
  }

  @override
  String toString() {
    return "Soy un gato y me llamo $name y tengo $age";
  }

  @override
  void makeNoise() {
    print('Meoww');
  }
  
  @override
  num calculate() {
    return age * 7;
  }
}
