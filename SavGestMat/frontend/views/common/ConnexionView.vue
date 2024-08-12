<script setup lang="ts">
import fondImage from '/images/fond_connexion.png';
import { accountService } from '@/utils/accountService';
import { onMounted, ref } from 'vue';
import { redirectBasedOnRole } from '@/utils/roleRedirect';

const errorMessage = ref('')

// Création d'un objet réactif pour l'utilisateur avec les propriétés email et password
const user = ref ({
    email: '',
    password:'',
});

onMounted (() => {
    if (accountService.isLogged()){
        const userRole = accountService.getUserRole();
        redirectBasedOnRole(userRole);
    }
})

const login = () => {
    accountService.login(user.value)
            .then((response: any) => {                
                accountService.saveToken(response.data.access);
                accountService.saveRefreshToken(response.data.refresh);                              
                window.location.reload()
            })
            .catch((error: any)=> {
                console.log(error.message);                
                if (error.code == 'ERR_NETWORK') {                    
                    errorMessage.value = "Une erreur réseau est survenue. Veuillez réessayer plus tard."
                }
                else if (error.code == 'ERR_BAD_REQUEST') {                    
                    errorMessage.value = "Adresse e-mail ou mot de passe incorrect."                    
                }
                else {
                    errorMessage.value = error.message;
                }                
            })
}
</script>

<template>
    <div class=" max-w-full w-auto min-h-screen bg-fixed bg-cover bg-center bg-no-repeat flex items-center justify-center font-opensans" 
        :style="{'backgroundImage':'url(' + fondImage +')'}">
        <div class="md:max-w-3xl w-5/12 2xl:w-1/2 h-full flex flex-col justify-center items-center backdrop-blur-2xl
            space-y-5 rounded-lg shadow-sm py-10 px-7 lg:px-14 bg-white/10">
            <h1 class="text-xl md:text-3xl 2xl:text-4xl font-opensans font-normal text-white mt-5 tracking-wide">
                Bienvenue
                <p class="text-yellow-500 text-lg mt-5 mb-3 text-center space-x-2"></p>
            </h1>
            <form id="login-form" method="post" class="w-full h-full space-y-8" @submit.prevent="login">
                <div class="w-full flex flex-row flex-wrap sm:max-md:space-y-2 md:justify-between">
                    <div class="w-full md:basis-[49%]">
                        <label id="label-username" class="sr-only capitalize" for="username">e-mail</label>
                        <input id="username" type="text" placeholder="E-mail" autocomplete="off"
                            class="form-input w-full h-10 rounded px-5 bg-transparent border border-blue-400 focus:outline
                            focus:outline-2 focus:outline-blue-500 focus:outline-offset-0 text-blue-200 placeholder:text-sm placeholder:text-gray-400" 
                            aria-labelledby="label-username" 
                            aria-required="true" v-model="user.email"/>
                    </div>
                    <div class="w-full md:basis-[49%]">
                        <label id="label-password" class="sr-only capitalize" for="password"> password </label>
                        <input id="password" type="password" placeholder="Password" autocomplete="off"
                            class="form-input w-full h-10 rounded px-5 bg-transparent border border-blue-400 focus:outline
                            focus:outline-2 focus:outline-blue-500 focus:outline-offset-0 text-blue-200 placeholder:text-sm placeholder:text-gray-400"
                            aria-labelledby="label-password" 
                            aria-required="true" v-model="user.password"/>
                    </div>
                </div>
                <hr class="h-px border-blue-200">
                
                <div class="w-full h-8 md:h-12 flex justify-center items-center mt-1">
                    <button type="submit" class="w-1/2 mx-auto h-full bg-sky-600 hover:bg-sky-700 text-blue-100
                    text-xs md:text-base font-semibold rounded-full focus:outline focus:outline-1 focus:outline-blue-500">
                    Se connecter 
                    </button>
                </div>                
                <div class="h-auto text-center">
                    <span v-if="errorMessage" class="text-xs md:text-base text-red-500 font-bold" >{{ errorMessage }}</span>
                </div>                
            </form>
            <div class="w-auto text-center space-y-2">
                <a href="#!" class="block text-xs md:text-sm text-sky-200 hover:text-sky-300">Mot de passe oublié ?</a>
                <a href="#!" class="block text-xs md:text-sm text-sky-200 hover:text-sky-300">Crée un compte</a>
            </div>  
        </div>    
    </div>
</template>
