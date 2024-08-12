import axios from "axios"
import router from "@/router"
import { accountService } from "./accountService"

// Crée une instance Axios avec une configuration de base, telle que l'URL de base. 
const Axios = axios.create({
    baseURL: 'http://localhost:8000'    
})

/* 
  Intercepte la requête, injecte le token d'authentification dans l'en-tête
  puis renvoie la requête modifiée.
*/
Axios.interceptors.request.use(request => {
    const token = accountService.getToken()
    if (token) {
        request.headers.Authorization = 'Bearer ' + token
    }
    return request
}, error => {
    return Promise.reject(error);
})

/* Intercepte la réponse  */
Axios.interceptors.response.use(response => {
    return response
}, async error => {
    const originalRequest = error.config;
    if (error.response && error.response.status === 401) {
        if (originalRequest.url.includes('/api/token/refresh/')) {
            accountService.logout()
            return Promise.reject(error);
        }

        // Vérifie si c'est un renouvellement de token
        if (!originalRequest._retry) {
            originalRequest._retry = true;

            try {
                const newToken = await accountService.getRefreshToken();
                //Met à jour le token dans la requête d'origine si le server a fourni un nouveau token
                if (newToken) {
                    originalRequest.headers.Authorization = 'Bearer ' + newToken;

                    // Renvoye la requête avec le nouveau token
                    return Axios(originalRequest);
                }
                else {
                    // Si le serveur n'a pas fourni de nouveau token, l'utilisateur est déconnecté
                    accountService.logout();                    
                }
            }
            catch (refreshError) {
                console.error("erreur lors du rafraichissement token : ", refreshError)
                accountService.logout();   
                return Promise.reject(refreshError)             
            }
        }    
        else {
            accountService.logout();            
        }    
    }
    return Promise.reject(error);
})

export default Axios