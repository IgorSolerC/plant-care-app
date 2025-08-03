import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, catchError, Observable, of, switchMap, tap } from 'rxjs';
import { User } from '../../domain/models/user';
import { Token } from '../../domain/models/token';
import { Router } from '@angular/router';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private http = inject(HttpClient);
  private router = inject(Router);

  private apiBaseUrl = environment.apiUrl;
  private tokenKey = 'auth_token';

  // BehaviorSubject to hold the current user state
  private currentUserSubject = new BehaviorSubject<User | null>(null);
  public currentUser$ = this.currentUserSubject.asObservable();

  // A simple observable for checking if the user is authenticated
  private isAuthenticatedSubject = new BehaviorSubject<boolean>(false);
  public isAuthenticated$ = this.isAuthenticatedSubject.asObservable();

  constructor() {
    window.addEventListener('storage', (event) => {
      if (event.key === this.tokenKey && !event.newValue) {
        // A token was removed from another tab. Force a logout in this tab.
        this.logout();
      }
    });
  }

  public checkInitialSession(): Observable<any> {
    const token = this.getToken();
    if (!token) {
      // If no token, there's nothing to do. Complete immediately.
      return of(null);
    }
    return this.http.get<User>(`${this.apiBaseUrl}/users/me`).pipe(
      tap({
        next: (user) => {
          this.currentUserSubject.next(user);
          this.isAuthenticatedSubject.next(true);
        },
        error: (err: any) => {
          // Token is invalid/expired, so log out
          this.logout();
        }
      }),
      // Use catchError to prevent the app from failing to load if the token is invalid
      catchError(() => {
        return of(null); // Ensure initialization completes successfully
      })
    );
  }

  // --- Core API Methods ---

  register(userData: any): Observable<User> {
    return this.http.post<User>(`${this.apiBaseUrl}/auth/register`, userData);
  }

  login(credentials: any): Observable<User> {
    const formData = new URLSearchParams();
    formData.set('username', credentials.email);
    formData.set('password', credentials.password);

    return this.http.post<Token>(`${this.apiBaseUrl}/auth/login`, formData.toString(), {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    }).pipe(
      // Once we have the token, switch to a new observable chain
      switchMap(tokenResponse => {
        this.saveToken(tokenResponse.access_token);
        // Fetch the user profile
        return this.http.get<User>(`${this.apiBaseUrl}/users/me`);
      }),
      // After the profile is fetched, update the state
      tap(user => {
        this.currentUserSubject.next(user);
        this.isAuthenticatedSubject.next(true);
      })
    );
  }

  getAllUsers(): Observable<User[]> {
    // The AuthInterceptor will automatically add the Bearer token to this request0
    return this.http.get<User[]>(`${this.apiBaseUrl}/auth/users/`);
  }

  loginWithGoogle(code: string): Observable<User> {
    return this.http.post<Token>(`${this.apiBaseUrl}/auth/google/login`, { code }).pipe(
      switchMap(tokenResponse => {
        this.saveToken(tokenResponse.access_token);
        return this.http.get<User>(`${this.apiBaseUrl}/users/me`);
      }),
      tap(user => {
        this.currentUserSubject.next(user);
        this.isAuthenticatedSubject.next(true);
      })
    );
  }

  logout(): void {
    localStorage.removeItem(this.tokenKey);
    this.currentUserSubject.next(null);
    this.isAuthenticatedSubject.next(false);
    this.router.navigate(['/auth']); // Navigate to a safe page after logout
  }

  // --- Helper Methods ---

  private handleAuthSuccess(token: string): void {
    this.saveToken(token);
    this.checkInitialSession(); // Fetch user profile after getting token
  }

  private saveToken(token: string): void {
    localStorage.setItem(this.tokenKey, token);
  }

  public getToken(): string | null {
    return localStorage.getItem(this.tokenKey);
  }
}
