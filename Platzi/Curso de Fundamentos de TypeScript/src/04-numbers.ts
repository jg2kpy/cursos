(() => {
  let productPrize = 100;
  productPrize = 12;
  console.log('productPrize' ,productPrize);

  let customerAge: number = 28;
  //  customerAge = customerAge + '1';
  customerAge = customerAge + 1;
  console.log('customerAge', customerAge);

  let productInStock: number;
  console.log('productInStock', productInStock);

  if(productInStock > 10){
    console.log('is greater');
  }

  let discount = parseInt('100');
  console.log('discount', discount);
  if(discount <= 200){
    console.log('apply');
  }else{
    console.log('no apply');
  }

  let hex = 0xfff;
  console.log('hex', hex);
  let bin = 0b1010;
  console.log('bin', bin);

  const myNumber: number = 10;

})();
