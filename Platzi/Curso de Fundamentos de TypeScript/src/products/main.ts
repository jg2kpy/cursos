import {createProduct, calcStock, products} from './product.service'

createProduct({
  name: 'Prod1',
  createdAt: new Date(1993,1,1),
  stock: 5,
  size: 'S'
})

createProduct({
  name: 'Prod2',
  createdAt: new Date(1993,1,1),
  stock: 6,
  size: 'XL'
})

console.log(products);
console.log(calcStock());
