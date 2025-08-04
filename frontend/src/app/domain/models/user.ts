import { GruposAssociados } from "./grupos-associados";

export interface User {
    id: number;
    email: string;
    full_name: string;
    is_active: boolean;
    grupos_associados: GruposAssociados[];
  }
