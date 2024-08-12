<script setup lang="ts">
import IconSociete from './icons/IconSociete.vue';
import IconLogout from './icons/IconLogout.vue';
import { accountService } from '@/utils/accountService';
import { onMounted, ref } from 'vue';
import ItemMenu from './ItemMenu.vue';

const userRole = ref('');


const logout = () =>{
  accountService.logout();  
}
onMounted (()=> {
  
  userRole.value = accountService.getUserRole();
  
})
</script>

<template>    
    <div class="flex-none w-1/5 md:w-60 bg-sky-800 text-white item-center justify-center md:pl-4">      
        <div class="flex item-center space-x-2 mt-8 md:scale-150 md:ml-6 md:pl-8">
            <IconSociete/>
            <span class="text-sm my-1 md:my-0 md:text-base font-semibold">GestMat</span>  
        </div>                      
        <hr class="md:absolute h-1 mt-8 w1/5 md:w-60 left-0">
        
          <ul class="mt-20 space-y-4">
            <ItemMenu/>           
          </ul>
          <div class="absolute bottom-10 left-0 right-0 w-60">
            <div @click="logout" class="flex item-center space-x-2 text-base font-semibold tracking-wide md:justify-center  cursor-pointer">
              <IconLogout class="text-cyan-100 scale-125 ml-10 md:ml-0"/>
              <span class="text-cyan-100 hidden md:block">Déconnexion</span>
            </div>            
          </div>
    </div>
</template>