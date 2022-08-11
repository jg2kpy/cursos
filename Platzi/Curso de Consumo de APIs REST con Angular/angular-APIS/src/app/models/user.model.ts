export interface User {
  id: string;
  name: string
  email: string;
  password: string;
}


export interface CreateProductDTO extends Omit<User, 'id'>{
}
