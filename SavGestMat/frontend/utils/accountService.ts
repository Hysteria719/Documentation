import Axios from "@/utils/axios-config";
import Cookies from 'js-cookie';
import router from "@/router";
import { jwtDecode } from "jwt-decode";

const REFRESH_TOKEN_COOKIE_NAME: string = 'refreshToken'
const expirationDate: Date = new Date();

// Ajoute une semaine
expirationDate.setDate(expirationDate.getDate() + 7);

const login = (credential: any) => {
    return Axios.post('api/token/', credential)
}

const logout = () => {
    localStorage.removeItem('token')
    Cookies.remove(REFRESH_TOKEN_COOKIE_NAME);
    window.location.reload();
}

const getToken = () => {
    return localStorage.getItem('token')
}

const getRefreshToken = () => {
    const refreshToken = Cookies.get(REFRESH_TOKEN_COOKIE_NAME);

    if (!refreshToken) {
        throw new Error('Refresh token non trouvé')
    }
    
    return Axios.post('/api/token/refresh/', {
        refresh: refreshToken,
    }).then((response) => {
        const newToken = response.data.access;                      

         // Mettre à jour le token dans le localStorage
         saveToken(newToken)         

         return newToken;
    })
    .catch((error) => {
        console.log("Erreur refresh token : ", error);

        if (error.response && error.response.status === 401) {
            accountService.logout();            
        }
    })
}

/* Sauvegarde le token dans le local storage */
const saveToken = (token: string) => {
    localStorage.setItem('token', token)
}

/* Sauvegarde le refresh token dans un cookie */
const saveRefreshToken = (refreshToken: string) => {
    
    // Enregistre le refresh token dans un cookie avec des options sécurisées
    Cookies.set(REFRESH_TOKEN_COOKIE_NAME, refreshToken, {
        secure: false, // Normalement, il faut le mettre sur true pour n'accepter que les connexions en HTTPS
        sameSite: 'Strict', // Limite l'envoie du cookie aux requête du même site
        httpOnly: false, // Si true rend le cookie inaccessible via Javascript
        expires: expirationDate,
    });
} 

// Fonction qui vérifie si l'utilisateur est connecté
const isLogged = () => {
    if (localStorage.getItem('token')) {
        return true
    }
    return false
}

const getUserRole = () => {
    const token = getToken()
    if (token) {
        const decodeToken: any = jwtDecode(token)
        const userRole = decodeToken.role;
        return userRole;
    }
    return null
}


export const accountService = {
    login,
    logout,
    getToken,
    getRefreshToken,
    saveToken,
    saveRefreshToken,
    isLogged,
    getUserRole
}