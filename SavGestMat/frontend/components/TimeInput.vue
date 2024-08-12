<script setup lang="ts">
import { ref } from 'vue';
import type { TimeOption } from '@/types/components';

const propsParams = defineProps<{
    timeOptions: TimeOption;
    modelValue: string;
}>();

const emit = defineEmits<{(e:'update:modelValue', value: string): void}>();
const time = ref( propsParams.modelValue || '');

const updateTime = () => {
    emit('update:modelValue', time.value)
}

</script>

<template>   
    <label :for="propsParams.timeOptions.id" class="block text-gray-600 text-sm font-bold mb-2">{{ propsParams.timeOptions.label }}</label> 
    <input type="time" v-model="time" :id="propsParams.timeOptions.id" :name="propsParams.timeOptions.name" 
        class="rounded-full bg-white text-sky-700 text-base font-semibold border-2 border-sky-300
        py-3 px-4 leading-tight focus:outline-none focus:ring-2 
        focus:ring-blue-500 focus:border-blue-500 shadow-sm" @input="updateTime">
</template>