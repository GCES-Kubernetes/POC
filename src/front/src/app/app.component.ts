import { Component } from '@angular/core';
import { BackendService } from './backend.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'poc';

  flaskMongoResponse : any
  service : any 

  constructor( service : BackendService) {
    this.service = service
    this.flaskMongoResponse = this.getFlaskMongo()
    console.log(this.flaskMongoResponse)
   }


   getFlaskMongo() {
    this.service.getDataFlaskMongo().subscribe((data: {data: null, messages: "", status: ""}) => {
      this.flaskMongoResponse = data['data']
      console.log(data)
    });
  }
}