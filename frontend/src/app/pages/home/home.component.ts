import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { CardTarefaComponent } from './card-tarefa/card-tarefa.component';
import { Tarefa } from '../../domain/models/tarefa';
import { TipoRega } from '../../domain/models/tipo-rega';
import { TarefaStatusEnum } from '../../domain/models/enums/tarefa-status.enum';
import { TipoAdubo } from '../../domain/models/tipo-adubo';
import { TipoLuz } from '../../domain/models/tipo-luz';
import { TipoVento } from '../../domain/models/tipo-vento';

@Component({
  selector: 'app-home',
  imports: [RouterModule,
    CardTarefaComponent,
    CommonModule
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {
  tarefas: Tarefa[] = [
    {
      id: 1,
      nomePlanta: 'Nome Planta Exemplo',
      descPlanta: 'Descrição breve exemplo',
      foto: 'https://picsum.photos/seed/1/200/300',
      dataProgramada: new Date(),
      status: TarefaStatusEnum.PENDENTE,
      tipoRega: {
        id: 1,
        nome: 'Pouco'
      } as TipoRega,
      tipoAdubo: {
        id: 1,
        nome: '10-10-10'
      } as TipoAdubo,
      tipoLuz: {
        id: 1,
        nome: 'Sol Pleno'
      } as TipoLuz,
    } as Tarefa,
    {
      id: 2,    
      nomePlanta: 'Nome Planta Exemplo',
      descPlanta: 'Descrição breve exemplo',
      foto: 'https://picsum.photos/seed/2/200/300',
      dataProgramada: new Date(),
      status: TarefaStatusEnum.PENDENTE,
      tipoRega: {
        id: 1,
        nome: 'Moderadamente'
      } as TipoRega,
      tipoVento: {
        id: 1,
        nome: 'Indiferente'
      } as TipoVento,
    } as Tarefa,
    {
      id: 3,   
      nomePlanta: 'Nome Planta Exemplo',
      descPlanta: 'Descrição breve exemplo',
      foto: 'https://picsum.photos/seed/3/200/300',
      dataProgramada: new Date(),
      status: TarefaStatusEnum.PULADO,
      tipoRega: {
        id: 1,
        nome: 'Moderadamete'
      } as TipoRega,
      tipoAdubo: {
        id: 1,
        nome: '10-10-10'
      } as TipoAdubo,
      tipoLuz: {
        id: 1,
        nome: 'Sol Pleno'
      } as TipoLuz,
      tipoVento: {
        id: 1,
        nome: 'Indiferente'
      } as TipoVento,
    } as Tarefa,
    {
      id: 4,   
      nomePlanta: 'Nome Planta Exemplo',
      descPlanta: 'Descrição breve exemplo',
      foto: 'https://picsum.photos/seed/4/200/300',
      dataProgramada: new Date(),
      status: TarefaStatusEnum.FEITO,
      tipoRega: {
        id: 1,
        nome: 'Muito'
      } as TipoRega,
    } as Tarefa,
  ]
}
