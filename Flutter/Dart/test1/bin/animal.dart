abstract class Animal{
  
  bool isMale = true;
  int _age = 0;

  Animal(){
    isMale = true;
  }

  String get sex => isMale ? "male": "female";

  set age(int value){
    if(value>0){
      _age = value;
    }
  }

  int get age => _age;

  void makeNoise(){
    print('Grrr');
  }
}
