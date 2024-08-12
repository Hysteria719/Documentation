interface Device {
    appareil_id: number;
    id: number;
    statut: string;
    utilisateur_id: number;
    appareil: {
        nom: string;
        num_serie: string;
        reference: string;
        proch_maintenance: Date;
        information: string; 
    }
}

interface DeviceSelected {
    id: number | null;
    nom: string;
    num_serie: string;
    reference: string;
    proch_maintenance: Date | null;
    information: string;
}

interface Filter {
    statut?: string;
    utilisateur_id?: number;
    appareil_id?: number;
}

export type {Device, DeviceSelected, Filter}