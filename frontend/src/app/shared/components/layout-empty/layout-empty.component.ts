import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NgxSpinnerModule } from 'ngx-spinner';

@Component({
  selector: 'app-layout-empty',
  imports: [RouterOutlet, NgxSpinnerModule],
  templateUrl: './layout-empty.component.html',
  styleUrl: './layout-empty.component.scss'
})

export class LayoutEmptyComponent {

}
