import { inject } from '@angular/core';
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NgxSpinnerModule } from 'ngx-spinner';
import { ThemeService } from './core/services/theme.service';

@Component({
  selector: 'app-root',
  imports: [
    RouterOutlet,
    NgxSpinnerModule,
  ],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  themeService = inject(ThemeService)
}
