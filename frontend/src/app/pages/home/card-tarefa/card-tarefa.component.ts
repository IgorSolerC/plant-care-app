import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Tarefa } from '../../../domain/models/tarefa';
import { LucideAngularModule, Leaf, Droplets, CircleCheckBig, SkipForward, Wind, Sun } from 'lucide-angular';
import { TarefaStatusEnum } from '../../../domain/models/enums/tarefa-status.enum';

import { Dialog } from 'primeng/dialog';


@Component({
  selector: 'app-card-tarefa',
  imports: [CommonModule,
    LucideAngularModule,
    Dialog
  ],
  templateUrl: './card-tarefa.component.html',
  styleUrl: './card-tarefa.component.scss'
})
export class CardTarefaComponent {
  @Input() tarefa!: Tarefa;

  readonly tarefaStatusEnum = TarefaStatusEnum;
  readonly Droplets = Droplets;
  readonly Leaf = Leaf;
  readonly Wind = Wind;
  readonly Sun = Sun;
  readonly CircleCheckBig = CircleCheckBig;
  readonly SkipForward = SkipForward;

  plantInfoVisible: boolean = false;

  showDialog() {
      this.plantInfoVisible = true;
  }
}