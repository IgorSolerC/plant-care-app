import { Component, inject } from '@angular/core';
import { AuthService } from '../../core/services/auth.service';
import { ToastrService } from 'ngx-toastr';
import { Observable } from 'rxjs';
import { User } from '../../domain/models/user';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [
  CommonModule
  ],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.scss'
})
export class ProfileComponent {
  private authService = inject(AuthService);
  private toastr = inject(ToastrService);

  public user$: Observable<User | null> = this.authService.currentUser$;
  public isAuthenticated$: Observable<boolean> = this.authService.isAuthenticated$;

  logout(): void {
    this.authService.logout();
    this.toastr.info('Você foi desconectado.', 'Até logo!');
  }

  formatarCodigoConvite(codigo: string): string {
    return codigo.substring(0,2) + '-' + codigo.substring(2,4) + '-' + codigo.substring(4,6);
  }
}
