import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpErrorResponse } from '@angular/common/http';

import { Product } from './../models/product.model';
import { CreateProductDTO, UpdateProductDTO } from './../models/product.model';

import { environment } from './../../environments/environment.prod'

@Injectable({
  providedIn: 'root'
})
export class ProductsService {

  private apiUrl = `${environment.API_URL}/api/products`;

  constructor(
    private http: HttpClient
  ) { }

  getAllProducts(limit?: number, offset?: number) {
    let params = new HttpParams();
    if(limit && offset){
      params.set('limit',limit)
      params.set('offset',offset)
    }
    return this.http.get<Product[]>(this.apiUrl, { params });
  }

  getProduct(id: string){
    return this.http.get<Product>(`${this.apiUrl}/${id}`)
  }

  getProductsByPage(limit: number, offset: number){
    return this.http.get<Product[]>(this.apiUrl, {
      params: { limit, offset }
    })
  }

  create(dto: CreateProductDTO){
    return this.http.post<Product>(this.apiUrl, dto);
  }

  update(id: string, dto: UpdateProductDTO){
    return this.http.put<Product>(`${this.apiUrl}/${id}`, dto);
  }

  delete(id: string){
    return this.http.delete<boolean>(`${this.apiUrl}/${id}`)
  }
}
