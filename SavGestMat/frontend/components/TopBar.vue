<script setup lang="ts">
import IconAlert from './icons/IconAlert.vue';
import IconUserCircle from './icons/IconUserCircle.vue';

const openModal = () => {
    console.log("affiche click");
}
</script>
<template>
    <div class="h-20 shadow-[0_.15rem_1.75rem_0_rgba(58,59,69,.15)] bg-white p-4">
        <div class="flex items-center justify-items-between mt-2">
            <div class="ml-auto flex space-x-9">
                <IconAlert @click="openModal" class="cursor-pointer"/>
                <IconUserCircle/>
            </div>
            
        </div>
        
    </div>
</template>