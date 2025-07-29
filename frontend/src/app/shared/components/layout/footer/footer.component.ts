import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { LucideAngularModule, User, ListTodo, Calendar, ClipboardList } from 'lucide-angular';

@Component({
  selector: 'app-footer',
  imports: [RouterModule, LucideAngularModule],
  templateUrl: './footer.component.html',
  styleUrl: './footer.component.scss'
})
export class FooterComponent {
  readonly ListTodo = ListTodo;
  readonly Calendar = Calendar;
  readonly ClipboardList = ClipboardList;
  readonly User = User;
}
