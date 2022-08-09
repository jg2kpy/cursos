(() => {
  const login = (data: { email: string, password: number }) => {
    console.log(data.email, data.password);
  }
  // login('junior@hotmail.com', '121212')
  login({
    email: 'junior@hotmail.com',
    password: 12
  })

  type Sizes = 'S' | 'M' | 'L' | 'XL';

  const products: any[] = [];

  const addProduct = (data: {
    title: string,
    createdAt: Date,
    stock: number,
    size?: Sizes
  }) => {
    products.push(data)
  }

  addProduct({
    title: 'Prod1',
    createdAt: new Date(1993,1,1),
    stock: 12,
    size: 'S'
  })

  console.log(products);
})();
