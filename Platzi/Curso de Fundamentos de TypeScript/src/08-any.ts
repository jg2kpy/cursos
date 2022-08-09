(() => {
  let myDynamicVar: any;

  myDynamicVar = 1000;
  myDynamicVar = null;
  myDynamicVar = {};
  myDynamicVar = '';

  myDynamicVar = 'Hola';
  const rta = (myDynamicVar as string)
  console.log(rta)

  myDynamicVar = 1212
  const rta2 = (<number> myDynamicVar).toFixed()
  console.log(rta2)

})();
