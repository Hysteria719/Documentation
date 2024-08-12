<script setup lang="ts">
import { ref } from 'vue';
import * as Icon from './icons/ImportsIcons'
import { accountService } from '@/utils/accountService.js';

const selectedItem = ref('');
const userRole = ref('');
const moveNameItem = ref('pl-9');
let pathUrl: string = ''; 
userRole.value = accountService.getUserRole();
const pathRole: string = "/" + userRole.value + "/"

let menuItems: any[] | null = [];

const selectItem = (itemId: string) => {
  selectedItem.value = itemId;    
};

const menuEmploye = [
  { id: 'dashboard', name: 'Dashboard', icon: Icon.IconDash, url:'/employe/dashboard' },
  { id: 'search', name: 'Recherche', icon: Icon.IconSearch, url:'/employe/search' },  
];

const menuAdmin = [
{ id: 'dashboard', name: 'Dashboard', icon: Icon.IconDash },
{ id: 'admin', name: 'Administration', icon: Icon.IconAdministration },
]
switch (userRole.value){
    case 'employe':
        selectedItem.value = 'dashboard'; 
        menuItems = menuEmploye;
        break;
    case 'admin':
        selectedItem.value = 'dashboard';
        menuItems = menuAdmin;
        moveNameItem.value = "pl-9 md:pl-4";
        break;
    default:
        menuItems = null
}
pathUrl = window.location.pathname;
pathUrl = pathUrl.replace(pathRole, "")
if (pathUrl !== '/'){
    selectedItem.value = pathUrl;
}
</script>
<template>
  
    <li v-for="item in menuItems" :key="item.id" class="relative">
        <RouterLink :to="item.url">
      <div class="ml-4 md:ml-0 w-16 md:w-52 absolute cursor-pointer select-none shadow-lg inset-0 rounded-lg bg-gray-700 text-white opacity-0 transition-opacity duration-300 ease-in-out" :class="{ 'bg-sky-300 opacity-25': selectedItem === item.id }"></div>
      <div @click="selectItem(item.id)" class="flex items-center cursor-pointer select-none space-x-4 text-base font-semibold tracking-wide  h-10" :class="moveNameItem">
        <component :is="item.icon" class="text-cyan-100 scale-125" />
        <span class="pl-2 hidden md:block text-cyan-100 scale-125">{{ item.name }}</span>
      </div>
      </RouterLink>  
    </li>    
    
</template>