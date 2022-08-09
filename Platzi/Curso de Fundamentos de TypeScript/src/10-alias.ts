(() => {
  type UserID = number | string
  let cedula: UserID;

  //Literal types
  type Sizes = 'S' | 'M' | 'L' | 'XL';
  let shirtSize: Sizes;
  shirtSize = 'M'
  shirtSize = 'L'
  shirtSize = 'XL'

  function greeting(myText: UserID, size: Sizes){
    if (typeof myText === 'string'){
      console.log(myText.toUpperCase());
    }
  }

  cedula = 1111
  greeting(cedula, 'M')

})();
