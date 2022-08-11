import { Component } from '@angular/core';

import { Product } from './models/product.model';



import { UsersService } from './services/users.service';
import { AuthService } from './services/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  imgParent = '';
  showImg = true;

  token = ''

  email = ''

  constructor(
    private authService: AuthService,
    private userService: UsersService
  ){

  }


  onLoaded(img: string) {
    console.log('log padre', img);
  }

  toggleImg() {
    this.showImg = !this.showImg;
  }

  createUser(){
    this.userService.create({
      name: 'jg2kpy',
      email: 'jg2kpy@email.com',
      password: '1212'
    })
    .subscribe(rta => {
      console.log(rta)
    })
  }

  login(){
    this.authService.login('jg2kpy@email.com','1212')
    .subscribe(rta => {
      this.token = rta.access_token
    })
  }

  getProfile(){
    this.authService.profile(this.token).
    subscribe(profile => {
      console.log(profile)
    })
  }
}
