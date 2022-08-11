import { Component, OnInit } from '@angular/core';

import { Product } from '../../models/product.model';
import { CreateProductDTO, UpdateProductDTO } from '../../models/product.model';

import { StoreService } from '../../services/store.service';
import { ProductsService, } from '../../services/products.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss']
})
export class ProductsComponent implements OnInit {

  myShoppingCart: Product[] = [];
  total = 0;
  products: Product[] = [];
  showProductDetail = false
  productChosen: Product = {
    id: '',
    price: 0,
    images: [],
    title: '',
    category: {
      id: 0,
      name: '',
      typeImg: ''
    },
    description: ''
  };

  limit = 10;
  offset = 0;

  statusDetail: 'loading' | 'sucess' | 'error' | 'init' = 'init';

  constructor(
    private storeService: StoreService,
    private productsService: ProductsService
  ) {
    this.myShoppingCart = this.storeService.getShoppingCart();
  }

  ngOnInit(): void {
    this.productsService.getProductsByPage(10, 0)
      .subscribe(data => {
        this.products = data;
      });
  }

  onAddToShoppingCart(product: Product) {
    this.storeService.addProduct(product);
    this.total = this.storeService.getTotal();
  }

  toggleProductDetail() {
    this.showProductDetail = !this.showProductDetail
  }

  onShowDetail(id: string) {
    this.statusDetail = 'loading'
    this.productsService.getProduct(id)
    .subscribe(data => {
      if(this.showProductDetail == false){
        this.toggleProductDetail();
        this.statusDetail = 'sucess'
      }
      this.productChosen = data;
    }, response => {
      console.log(response.error.message);
      this.statusDetail = 'error'
    })
  }

  createNewProduct() {
    const product: CreateProductDTO = {
      title: 'Nuevo Producto',
      description: 'bla bla bla',
      images: ['https://placeimg.com/640/480/any'],
      price: 1000,
      categoryId: 2,
    }
    this.productsService.create(product)
    .subscribe(data => {
      console.log('created ', data)
    });
  }

  updateProduct(){
    const changes:UpdateProductDTO = {
      title: 'nuevo title'
    }
    const id = this.productChosen.id;
    this.productsService.update(id, changes).subscribe(data => {
      const productIndex = this.products.findIndex(item => item.id === id)
      this.products[productIndex] = data
      this.productChosen = data
    })
  }

  deleteProduct(){
    const id = this.productChosen.id
    this.productsService.delete(id).subscribe(() => {
      const productIndex = this.products.findIndex(item => item.id === id)
      this.products.splice(productIndex, 1)
      this.showProductDetail = false
    })
  }

  loadMore(){
    this.productsService.getProductsByPage(this.limit, this.offset)
    .subscribe(data => {
      this.products = this.products.concat(data);
      this.offset += this.limit
    });
  }
}
