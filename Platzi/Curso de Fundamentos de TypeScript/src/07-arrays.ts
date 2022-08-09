(() => {
  let prices = [1,2,3, 'hola', true];
  prices.push(123);

  let products = ['hola', true];
  products.push(false)

  let mixed: (number | string | boolean | Object)[] = ['hola', true];
  mixed.push(12)
  mixed.push('12')
  mixed.push([])

  let numbers = [1,2,3];
  numbers.map(item => item * 2)
})();
