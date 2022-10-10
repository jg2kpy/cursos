import 'cat.dart';
import 'duck.dart';

void main() {
  var cat1 = Cat('bala');
  cat1.age = 10;
  // print(cat1);
  // print(cat1.name);
  cat1.pur();
  cat1.makeNoise();

  var duck1 = Duck();
  duck1.age = 4;
  // print(duck1);
  duck1.makeNoise();

  var animals = [];
  animals.add(cat1);
  animals.add(duck1);
  animals.add(Cat('Fluffly'));

  for(var animal in animals){
    print(animal);
    if(animal is Cat){
      animal.pur();
    }
  }
}
