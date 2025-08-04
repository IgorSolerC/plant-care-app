import { Injectable } from '@angular/core';
import { HttpClient as httpClient, HttpContext } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class GrupoService {
  private apiUrl = `${environment.apiUrl}/grupos`;

  constructor(private http: httpClient) { }


}
