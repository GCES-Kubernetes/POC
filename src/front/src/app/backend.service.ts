import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BackendService {

  constructor(private http: HttpClient) { }

  getDataFlaskMongo(): Observable<any> {
    let header: HttpHeaders = new HttpHeaders();
    header = header.append("Content-Type", "application/json");
    return this.http.get('flask/mongo', { headers: header })
  }
}
