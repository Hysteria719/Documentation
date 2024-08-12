<script setup lang="ts">
import type { ButtonAction } from '@/types/components';
const propsParams = defineProps<{
    buttonOptions : ButtonAction
}>()
const emit = defineEmits(['submitButton'])

const handleClick = () => {
    emit('submitButton');
}
</script>

<template>
    <button type="button" class=" h-10 bg-blue-200 py-1 px-4 rounded-full
                            text-white hover:bg-blue-700 hover:ring-2 hover:ring-blue-300 hover:ring-offset-2
                            focus:outline focus:outline-0 focus:outline-blue-300 
                            focus:outline-offset-1 active:text-blue-700  disabled:text-blue-100 
                            disabled:pointer-events-none duration-100 select-none" 
                            :class="[{'bg-blue-500': propsParams.buttonOptions.isActive},{'bg-blue-100 disabled:text-white': !propsParams.buttonOptions.isActive}]" 
                            :disabled="!propsParams.buttonOptions.isActive" @click="handleClick">
    {{ propsParams.buttonOptions.title }}</button>
                            
</template>