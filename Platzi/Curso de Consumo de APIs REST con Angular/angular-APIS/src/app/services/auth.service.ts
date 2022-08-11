import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams, HttpErrorResponse } from '@angular/common/http';
import { environment } from './../../environments/environment.prod'
import { User, CreateProductDTO } from './../models/user.model';
import { Auth } from './../models/auth.model';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private apiUrl = `${environment.API_URL}/api/auth`;

  constructor(
    private http: HttpClient
  ) { }

  login(email: string, password: string){
    return this.http.post<Auth>(`${this.apiUrl}/login`, {
      email,
      password
    })
  }

  profile(token: string){
    // const headers = new HttpHeaders();
    // headers.set('Authorization', `Bearer ${token}`);
    return this.http.get<User>(`${this.apiUrl}/profile`,{
      headers: {
        Authorization: `Bearer ${token}`
        //'Content-type': 'application/json'
      }
    });
  }
}
