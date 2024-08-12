
<script setup lang="ts">
  
  import IconChevronLeft from './icons/IconChevronLeft.vue';
  import IconChevronRight from './icons/IconChevronRight.vue';

  import type { Pagination } from '@/types/pagination';

  import { computed, defineEmits, ref } from 'vue';

  const propsParam = defineProps <{
    pagination : Pagination | null 
  }>();

  const emit = defineEmits(['pagination-offset'])

  
  const count = computed(() => propsParam.pagination?.count ?? 0); 
  const limit = computed(() => propsParam.pagination?.limit ?? 1)
  const totalPages = computed(() => Math.ceil(count.value / limit.value));
  const currentPage = ref<number>(1);       
  const startIndex = computed(() => (currentPage.value - 1) * limit.value + 1);     
  const endIndex = computed(() => Math.min(currentPage.value * limit.value, count.value))

  const goToPage = (page: number) => {
    if (currentPage.value != page) {
      const offset = (page - 1 )* limit.value;
      emit('pagination-offset', offset);
      console.log("offest Pg : ", offset)
    }
    currentPage.value = page;
  } 

  const goToNextPage = () => {

    if (currentPage.value < totalPages.value) {
      currentPage.value += 1      
    }        
    const url = propsParam.pagination?.next
    if (url) {
      const params = new URLSearchParams(url.split('?')[1]);
      const offset = params.get('offset');
      emit('pagination-offset', offset);      
    }    
  }

  const goToPreviousPage = () => {
    if (currentPage.value != 1) {
      currentPage.value -=1
    }
    const url = propsParam.pagination?.previous
    if (url) {
      const params = new URLSearchParams(url.split('?')[1]);
      const offset = params.get('offset');
      emit('pagination-offset', offset);
    }    
  }  

  </script>
<template>
    <div class="flex items-center justify-between border-slate-200 bg-slate-50 px-4 pt-8 sm:px-6">
      <div class="flex flex-1 justify-between sm:hidden">
        <a @click.prevent="goToPreviousPage()" href="#" class="relative inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Previous</a>
        <a @click.prevent="goToNextPage()" href="#" class="relative ml-3 inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Next</a>
      </div>
      <div class="hidden sm:flex sm:flex-1 sm:items-center sm:justify-between">
        <div>
          <p class="font-opensans text-xs text-gray-400 font-medium">
            Affichage de
            {{ ' ' }}
            <span class="font-medium">{{ startIndex }}</span>
            {{ ' ' }}
            à
            {{ ' ' }}
            <span class="font-medium">{{ endIndex }}</span>
            {{ ' ' }}
            sur
            {{ ' ' }}
            <span class="font-medium">{{ count }}</span>
            {{ ' ' }}
            résultats
          </p>
        </div>
        <div>
          <nav class="isolate inline-flex -space-x-px rounded-md shadow-sm" aria-label="Pagination">
            <a @click.prevent="goToPreviousPage()" href="#" class="relative inline-flex items-center rounded-l-md px-2 py-2 text-teal-600 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0">
              <span class="sr-only">Previous</span>
              <IconChevronLeft class="h-5 w-5" aria-hidden="true" />
            </a>
            
            <a v-for="page in totalPages" :key="page" :href="`#`" :class="[
        'relative inline-flex items-center px-4 py-2 text-xs text-slate-400 font-semibold ring-1 ring-inset ring-gray-300 hover:bg-gray-0 focus:outline-offset-0',
        { 'bg-indigo-600 text-slate-100': page === currentPage, 'text-gray-900': page !== currentPage }]" aria-current="page" @click.prevent="goToPage(page)">{{ page }}</a>
           
            <a @click.prevent="goToNextPage()" href="#" class="relative inline-flex items-center rounded-r-md px-2 py-2 text-teal-600 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0">
            
              <span class="sr-only">Next</span>
              <IconChevronRight class="h-5 w-5" aria-hidden="true" />
            </a>
          </nav>
        </div>
      </div>
    </div>    
  </template>
  
  