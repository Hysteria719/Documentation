<script setup lang="ts">
import type { ModalOption } from '@/types/components';
const propsParam = defineProps<{
    modalOptions : ModalOption        
}>()
const emit = defineEmits(['closeModal','submitButton'])
</script>

<template>
    <div v-if="propsParam.modalOptions.isVisible" class="fixed inset-0 flex items-center justify-center z-50">      
      <div class="fixed inset-0 bg-black bg-opacity-50" @click="emit('closeModal')"></div>            
      <div class="bg-slate-50 rounded-lg shadow-lg max-w-xl w-full p-6 z-10">
        <h2 class="uppercase text-blue-900 font-semibold tracking-wide text-base mb-4 border-b border-slate-200">{{ propsParam.modalOptions.title }}</h2>
        <div class="mb-4">         
          <slot></slot>
        </div>
        <div class="flex justify-end border-t border-slate-200">
          <button @click="emit('closeModal')" class="bg-slate-200 text-gray-800 capitalize tracking-wide hover:bg-slate-300 font-bold py-2 px-4 rounded-lg mt-4">
            {{ propsParam.modalOptions.closeButtonText }}
          </button>
          <button v-if="modalOptions.submitButtonText" @click="emit('submitButton')" class="mt-4 ml-4 bg-blue-700 capitalize text-white font-bold 
                                                                                            tracking-wide hover:bg-blue-900 py-2 px-4 rounded-lg">
            {{ propsParam.modalOptions.submitButtonText }}
          </button>
        </div>
      </div>
    </div>
  </template>