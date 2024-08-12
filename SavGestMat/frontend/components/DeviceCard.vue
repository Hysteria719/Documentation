<script setup lang="ts">
import type { DeviceSelected } from '@/types/device';
const propsParam = defineProps<{
    deviceSelected: DeviceSelected
}>()

</script>

<template>
    <div class="uppercase font-semibold text-sm text-sky-600 font-opensans tracking-wider">
                       <p><span class="font-semibold text-gray-400">Nom :</span>{{ propsParam.deviceSelected.nom }}</p>
                       <p><span class="font-semibold text-gray-400">Numéro de série :</span>{{ propsParam.deviceSelected.num_serie }}</p>
                       <p><span class="font-semibold text-gray-400">Référence :</span>{{ propsParam.deviceSelected.reference }}</p>
                       <p><span class="font-semibold text-gray-400">Prochaine maintenance :</span>{{ propsParam.deviceSelected.proch_maintenance }}</p>
                       <p class="mt-2"><span class="underline decoration-1 font-semibold text-gray-400">Informations</span></p>
                        <p>{{ propsParam.deviceSelected.information }}</p>
                    </div>   
</template>