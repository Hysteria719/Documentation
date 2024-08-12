import Axios from "./axios-config";
import type { Filter } from "@/types/device";
import type { PageSelected } from "@/types/pagination";

const url:string = '/api/employe/'

const getHeaders = () => {
    return {
        'Content-Type': 'application/json'
    }
}

const getDevices = (pageSelected: PageSelected, filter?: Filter) => {        
   let path:string = url + 'dashboard/'

    if (pageSelected.limit) {        
        path += '?limit=' + pageSelected.limit
    }
    if (pageSelected.offset) {
        path += '&offset=' + pageSelected.offset
    }
    if (filter && filter.statut) {
        path += '&statut=' + filter.statut
    } 
    if (filter && filter.appareil_id) {
        path += '&deviceId=' + filter.appareil_id
    }           
    return Axios.get(path)
    .then((response) => {        
        return response.data;
    })
    .catch((error) => {
        console.log("Erreur : ", error)
        throw error
    })
}

const getReservation = (deviceId: number | null) => {
    let path:string = url + 'reservation/';

    if (deviceId) {
        path += '?&deviceId=' + deviceId
    }
    return Axios.get(path)
    .then((response) => {
        return response.data
    })
    .catch((error) => {
        console.log("Erreur: ", error)
        throw error
    })
}

export const employeService = {
    getDevices,
    getReservation
}