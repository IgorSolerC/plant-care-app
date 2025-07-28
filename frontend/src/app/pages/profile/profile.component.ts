import { Component, inject } from '@angular/core';
import { AuthService } from '../../core/services/auth.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-profile',
  imports: [],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.scss'
})
export class ProfileComponent {
  private authService = inject(AuthService);
  private toastr = inject(ToastrService);

  logout(): void {
    this.authService.logout();
    this.toastr.info('Você foi desconectado.', 'Até logo!');
  }
}
