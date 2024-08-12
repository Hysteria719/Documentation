<script setup lang="ts">
import TableDevice from '@/components/TableDevice.vue'
import PaginaTion from '@/components/PaginaTion.vue';
import { onMounted, ref } from 'vue';
import { employeService } from '@/utils/employe-service';

import type { Device, Filter } from '@/types/device';
import type { Pagination, PageSelected } from '@/types/pagination';

const stateYourDevice = ref("yourDevice")
const stateFreeDevice = ref("free")
const devicesBorrowed = ref<Device[]>([])
const devicesFree = ref<Device[]>([])
const filterTabYourDevice = ref<Filter>({
    statut: 'vosAppareils' 
})
const paginationYourDevice = ref<Pagination | null>(null)
const paginationFreeDevice = ref<Pagination | null>(null)
const selectedYourDevicesPage = ref<PageSelected>({
    offset: 0,
    limit: 1
})
const selectedFreeDevicesPage = ref<PageSelected>({
    offset: 0,
    limit: 2
})

const fetchDataDevicesBorrowed = async () => {
   const dataDevicesBorrowed = await employeService.getDevices(selectedYourDevicesPage.value, filterTabYourDevice.value);      
   devicesBorrowed.value = dataDevicesBorrowed.results;          

   paginationYourDevice.value = {
    count: dataDevicesBorrowed.count,
    next: dataDevicesBorrowed.next,
    previous: dataDevicesBorrowed.previous,
    limit: selectedYourDevicesPage.value.limit
   }         
   
}
const fetchDataDevicesFree = async () => {
    const dataDevicesFree = await employeService.getDevices(selectedFreeDevicesPage.value);
    devicesFree.value = dataDevicesFree.results;
    
    paginationFreeDevice.value = {
    count: dataDevicesFree.count,
    next: dataDevicesFree.next,
    previous: dataDevicesFree.previous,
    limit: selectedFreeDevicesPage.value.limit
   }
}

onMounted (()=>{
    fetchDataDevicesBorrowed();
    fetchDataDevicesFree();
})
const handlePageChangeDevicesBorrowed = (offset: number) => {    
    selectedYourDevicesPage.value.offset = offset
    fetchDataDevicesBorrowed()
    console.log("offset yourdevice : ", offset)
}
const handlePageChangeDevicesFree = (offset: number) => {    
    selectedFreeDevicesPage.value.offset = offset
    fetchDataDevicesFree()
    console.log("offset FreeDevice : ", offset)
}
</script>

<template>
    <div class="p-8">
        <div class="w-full bg-white rounded font-opensans shadow-[0_.15rem_1.75rem_0_rgba(58,59,69,.15)]" >
            <div class="w-full space-y-0 p-4 rounded-t bg-slate-50">
                <div class="w-full flex flex-row justify-between items-center">
                    <h1 class="uppercase text-blue-900 font-semibold tracking-wide text-sm">Vos appareils</h1>
                </div>
                <TableDevice :stateDevice="stateYourDevice" :tabDevice="devicesBorrowed"/>
                <PaginaTion :pagination="paginationYourDevice" @pagination-offset="handlePageChangeDevicesBorrowed"/>
            </div>            
        </div>
    </div>
    <div class="p-8">
        <div class="w-full bg-white rounded font-opensans shadow-[0_.15rem_1.75rem_0_rgba(58,59,69,.15)]" >
            <div class="w-full space-y-0 p-4 rounded-t bg-slate-50">
                <div class="w-full flex flex-row justify-between items-center">
                    <h1 class="uppercase text-blue-900 font-semibold tracking-wide text-sm">Appareils libre</h1>
                </div>
                <TableDevice :stateDevice="stateFreeDevice" :tabDevice="devicesFree"/>
                <PaginaTion :pagination="paginationFreeDevice" @pagination-offset="handlePageChangeDevicesFree"/> 
            </div>            
        </div>
    </div>

    
</template>