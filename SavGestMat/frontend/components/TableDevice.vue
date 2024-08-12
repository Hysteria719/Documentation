<script setup lang="ts">
import IconEye from './icons/IconEye.vue';
import ToolTip from './ToolTip.vue';
import { useRouter } from 'vue-router';
import { onBeforeMount, onMounted, ref } from 'vue';
import { pageUtils } from '@/utils/pageUtils';

import type { Device } from '@/types/device';

const router = useRouter();
const tableContainer = ref<any>(null)
const isActiveButton = ref<boolean>(false)
const hoverBgRow = ref<string>('hover:bg-sky-200')
const idDevice = ref<number | null>()

const handleClickOutside = (event: any) => {
    if (tableContainer.value && !tableContainer.value.contains(event.target)) {
        stopClick();
    }
}

onMounted(() => {
    document.addEventListener('click', handleClickOutside);
})
onBeforeMount(() => {
    document.removeEventListener('click', handleClickOutside);
})

const propsParam = defineProps<{
    state?: string
    stateDevice : string
    tabDevice : Device[]    
}>();
const titleBtn = ref('') 
const selectedItemId = ref<number | null>(null)

switch (propsParam.stateDevice){
    case 'free' :
        titleBtn.value = 'Réserver'
        break;
    case 'yourDevice' :
        titleBtn.value = 'Libérer'
        break;
}
const selectRow = (item: Device) => {
    selectedItemId.value = item.id       
    //deviceSelected.value.appareil_id = item.appareil_id
    idDevice.value = item.appareil_id
    isActiveButton.value = true    
    hoverBgRow.value = 'hover:bg-sky-200'        
    /*
    deviceSelected.value.nom = item.appareil.nom
    deviceSelected.value.num_serie = item.appareil.num_serie
    deviceSelected.value.reference = item.appareil.reference
    deviceSelected.value.proch_maintenance = item.appareil.proch_maintenance
    deviceSelected.value.informations = item.appareil.information
    */
}
const stopClick = () => {
    selectedItemId.value = null       

    idDevice.value = null

    //deviceSelected.value.appareil_id = null
    
    isActiveButton.value = false    
}
const submitButton = () => {
    if (propsParam.stateDevice === 'yourDevice') {
        console.log("Libérer")
    }  
    if (propsParam.stateDevice === 'free') {
        console.log("Réserver")
        router.push({
            name:'reservation_employe',
            query: {id: idDevice.value}
        })
        /*       
        router.push({
            name:'reservation_employe',
            query: {
                id: deviceSelected.value.appareil_id,
                name: deviceSelected.value.nom,
                reference: deviceSelected.value.reference,
                serialNumber: deviceSelected.value.num_serie,
                maintenance: pageUtils.formatDate(deviceSelected.value.proch_maintenance),
                informations: deviceSelected.value.informations
            }
        })*/
    }
    
}
</script>

<template>    
    <div class="max-w-xs sm:max-w-md md:max-w-xl lg:max-w-none border-slate-200 bg-slate-50" ref="tableContainer">
        <div class="w-full py-4">
            <div class="">
                <button type="button" class="h-10 bg-blue-200 py-1 px-4 rounded-full
                    text-white hover:bg-blue-700 hover:ring-2 hover:ring-blue-300 hover:ring-offset-2
                    focus:outline focus:outline-0 focus:outline-blue-300 
                    focus:outline-offset-1 active:text-blue-700  disabled:text-blue-100 
                    disabled:pointer-events-none duration-100 select-none" 
                    :class="[{'bg-blue-500': isActiveButton},{'bg-blue-100 disabled:text-white': !isActiveButton}]" 
                    :disabled="!isActiveButton" @click="submitButton">{{ titleBtn }}</button>
            </div>
        </div>
        <div class="py-1"></div>              
        <div class="flex items-center justify-between overflow-auto lg:overflow-hidden "> 
        <table class="border-b">
            <thead class="border-b border-slate-200 bg-slate-50 ">
                <tr class="uppercase text-[11px] text-gray-400 font-opensans tracking-wider">
                    <th scope="col" class="text-left px-4 py-2 font-semibold cursor-pointer select-none w-80">Modèle</th>
                    <th scope="col" class="text-left px-4 py-2 font-semibold cursor-pointer select-none w-80">Num Série</th>
                    <th scope="col" class="text-left px-4 py-2 font-semibold cursor-pointer select-none w-80">Référence</th>
                    <th scope="col" class="text-left px-4 py-2 font-semibold cursor-pointer select-none w-60">Proch Maintenance</th>
                    <th scope="col" class="text-left px-4 py-2 font-semibold cursor-pointer select-none w-24">Information</th>
                    <th class="w-60"></th>
                </tr>
            </thead>            
            <tbody class="font-opensans text-base cursor-pointer">                                         
               <tr class="border-b last:border-none border-gray-100 text-gray-600 select-none" 
               :class="[
                    selectedItemId === item.id ? 'bg-blue-300' : 'bg-white hover:bg-sky-50',
                    selectedItemId === item.id && 'hover:bg-blue-300'
                ]"
                tabindex="0" v-for="item in tabDevice" :key="item.id" @click="selectRow(item)">
                    <td class="text-left pl-4"> <span>{{ item.appareil.nom }}</span></td>
                    <td class="text-left pl-4 py-2">{{ item.appareil.num_serie }}</td>
                    <td class="text-left pl-4 py-2">{{ item.appareil.reference }}</td>
                    <td class="text-left pl-4">{{ pageUtils.formatDate(item.appareil.proch_maintenance) }}</td>
                    <td class="text-left flex justify-center py-4"><ToolTip :message="item.appareil.information"><IconEye v-if="item.appareil.information"/></ToolTip> </td>
                    <td></td>                    
                </tr>                    
            </tbody>
        </table>               
    </div>    
    </div>
</template>