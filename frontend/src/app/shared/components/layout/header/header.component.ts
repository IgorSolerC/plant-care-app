import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { LucideAngularModule, Sprout, Plus } from 'lucide-angular';

@Component({
  selector: 'app-header',
  imports: [
    CommonModule,
    RouterModule,
    LucideAngularModule,
  ],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent { 
  readonly Sprout = Sprout;
  readonly Plus = Plus;
}
