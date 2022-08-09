(() => {
  type Sizes = 'S' | 'M' | 'L' | 'XL';

  function createProductToJson(
    title: string,
    createdAt: Date,
    stock: number,
    size: Sizes
  ) {
    return{
      title,
      createdAt,
      stock,
      size
    }
  }

  const createProductToJsonV2 = (
    title: string,
    createdAt: Date,
    stock: number,
    size?: Sizes
  ) => {
    return{
      title,
      createdAt,
      stock,
      size
    }
  }

  const producto1 = createProductToJsonV2('P1', new Date(), 12);
  console.log(producto1);
  console.log(producto1.title);
  console.log(producto1.stock);

})();
