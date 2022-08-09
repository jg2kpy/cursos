(() => {
  let cedula: number | string;
  cedula = 1212
  cedula = 'ass'

  function greeting(myText: number | string){
    if (typeof myText === 'string'){
      console.log(myText.toUpperCase());
    }else{
      console.log(myText.toFixed(1));
    }
  }

  greeting('asa')
  greeting(12.12)

})();
