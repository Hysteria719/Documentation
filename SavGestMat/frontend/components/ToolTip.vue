<script setup lang="ts">
const params = defineProps<{
    message: string
}>();

</script>

<template>
    <div class="tooltip"><slot></slot>
    <span class="tooltiptext"> {{ params.message }} </span>
</div>    
</template>

<style>

.tooltip {
  position: relative;
  display: inline-block;  
}


.tooltip .tooltiptext {
  visibility: hidden;
  width: 220px;
  max-height: 50px;
  background-color: #555;
  color: #ffffff;
  text-align: center;
 
  border-radius: 6px;
  padding-top: 0px;


  position: absolute;
  z-index: 1;
  top: -75%;
  left: -110%;
  margin-left: -210px;

  
  opacity: 0;
  transition: opacity 0.3s;
}


.tooltip .tooltiptext::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -5px;
  border-width: 0px;
  border-style: solid;
  border-color: #555 transparent transparent transparent;
}


.tooltip:hover .tooltiptext {
  visibility: visible;
  opacity: 1;
}

</style>