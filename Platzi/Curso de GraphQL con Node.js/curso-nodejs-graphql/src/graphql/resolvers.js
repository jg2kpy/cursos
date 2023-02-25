const { getProduct, getProducts, addProduct, updateProduct, deleteProduct } = require('./product.resolvers.js')

const resolvers = {
  Query: {
    hello: () => 'hello world',
    getPerson: (_, args) => `Hello, my name is ${args.name}, I'm ${args.age} years old!`,
    getInt: (_, args) => args.age,
    getFloat: (_, args) => args.price,
    getString: () => 'hola',
    getBoolean: () => true,
    getID: () => '123',
    getNumbers: (_, args) => args.numbers,
    product: getProduct,
    products: getProducts,
  },
  Mutation: {
    addProduct,
    updateProduct,
    deleteProduct
  }
}

module.exports = resolvers
