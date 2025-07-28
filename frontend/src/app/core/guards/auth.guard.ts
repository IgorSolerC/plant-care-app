import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { map, Observable, take } from 'rxjs';

export const authGuard: CanActivateFn = (route, state): Observable<boolean> => {
  const authService = inject(AuthService);
  const router = inject(Router);

  return authService.isAuthenticated$.pipe(
    take(1), 
    map(isAuthenticated => {
      if (isAuthenticated) {
        return true; // User is authenticated, allow access
      }
      
      // User is not authenticated, redirect to the login page
      router.navigate(['/auth']);
      return false;
    })
  );
};