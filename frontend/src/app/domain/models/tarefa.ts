import { TarefaStatusEnum } from "./enums/tarefa-status.enum";
import { TipoAdubo } from "./tipo-adubo";
import { TipoLuz } from "./tipo-luz";
import { TipoVento } from "./tipo-vento";
import { TipoRega } from "./tipo-rega";

export interface Tarefa {
    // core
    nomePlanta: string;
    descPlanta: string;
    foto: string;
    dataProgramada: Date;
    status: TarefaStatusEnum;

    // else
    tipoRega: TipoRega;
    tipoAdubo?: TipoAdubo;
    tipoLuz?: TipoLuz;
    tipoVento?: TipoVento;
}
