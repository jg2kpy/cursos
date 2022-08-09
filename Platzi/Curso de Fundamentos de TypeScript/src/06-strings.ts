(() => {
  let productTitle = 'My amazing product';
  productTitle = 'My amazing product changed';
  console.log('productTitle', productTitle);
  let productPrize = 100;
  let isNew = true;

  const productDescription = "I'm bla bla ass"
  console.log('productDescription', productDescription);

  const summary = `
    title: ${productTitle}
    description: ${productDescription}
    price: ${productPrize}
    is new: ${isNew}
  `
  console.log(summary);

})();
