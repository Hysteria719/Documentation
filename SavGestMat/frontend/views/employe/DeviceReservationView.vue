<script setup lang="ts">
import { onMounted, ref } from 'vue';
import DeviceCard from '@/components/DeviceCard.vue';
import FullCalendar from '@fullcalendar/vue3';
import dayGridPlugin from '@fullcalendar/daygrid';
import interactionPlugin from '@fullcalendar/interaction';
import { useRoute } from 'vue-router';
import ActionButton from '@/components/ActionButton.vue';
import ReservationModal from '@/components/ModalWindow.vue';
import TimeInput from '@/components/TimeInput.vue';
import { employeService } from '@/utils/employe-service';
import { pageUtils } from '@/utils/pageUtils';

import type { PageSelected } from '@/types/pagination';
import type { DeviceSelected, Filter } from '@/types/device';
import type { SelectedDate } from '@/types/reservation';
import type { ButtonAction, ModalOption, TimeOption } from '@/types/components';
import type { CalendarOptions } from '@fullcalendar/core/index.js';

const reservationEvents = ref<Event[]> ([]);
const route: any = useRoute();
const selectedDate = ref<SelectedDate>({
    dateStart:'',
    dateEnd: ''    
})
const pagination = ref<PageSelected>({
    offset: 0,
    limit: 1
})
const filterDevice = ref<Filter>({
     appareil_id: route.query.id 
})

// paramètre par défaut pour le composant TimeInput
const startTimeOption = ref<TimeOption>({
    id: '1',
    label: "Emprunter l'appareil",
    name: 'startTime',    
    selectedTime: '08:30'
})
// paramètre par défaut pour le composant TimeInput
const endTimeOptions = ref<TimeOption>({
    id: '2',
    label: "Rendre l'appareil",
    name: 'endTime',    
    selectedTime: '16:00'
})

const optionModal = ref<ModalOption>({
    closeButtonText: "Annuler",
    submitButtonText: "Réserver",
    isVisible: false,
    title: "Confirmation"
})
const deviceInformations = ref<DeviceSelected>({
    id: route.query.id,
    nom: '',
    num_serie: '',
    information: '',
    proch_maintenance: null,
    reference: ''
})

const buttonOptions = ref<ButtonAction>({
    title: 'Réserver',
    isActive: false
})

const fetchData = async () => {
    const dataDevice = await employeService.getDevices(pagination.value, filterDevice.value)
    deviceInformations.value = dataDevice.results[0].appareil    
    const data = await employeService.getReservation(route.query.id)    
    reservationEvents.value = data.map((reservation: {
        date_fin: string;
        date_debut: string; statut: string; 
}) => {
        let title = '';
        let color = '';
        let textColor = '';

        switch (reservation.statut) {
            case 'en_attente':
                title='Demande en attente';
                color = '#F5D300';
                textColor = '#000000';
                break;
            case 'accepte':
                title='Indisponible';
                color= '#14B8A6';
                textColor= 'white'
                break;
        }
        console.log("ReservationMap : ", reservation);
        return {
            title,
            start: reservation.date_debut,            
            end: reservation.date_fin,            
            backgroundColor: color,
            borderColor: color,
            textColor: textColor
        }
    })    
} 
onMounted(() => {
    fetchData();
    
})
const submitBorrow = () => {        
    const startTime = startTimeOption.value.selectedTime
    const endTime = endTimeOptions.value.selectedTime 
    const startDate = selectedDate.value.dateStart
    const endDate = selectedDate.value.dateEnd

    console.log('dateDepart : ', startDate, ' à ',startTime)
    console.log('dateFin : ', endDate, ' à ',endTime)
    console.log("Soumettre la réservation") 
    
}
const openModal = () => {
    optionModal.value.isVisible = true;
}
const closeModal = () => {
    optionModal.value.isVisible = false;
}
const calendarOptions = ref<CalendarOptions>({
    locale: 'locale',
    timeZone: 'locale',
    plugins: [dayGridPlugin, interactionPlugin],
    initialView: 'dayGridMonth',
    selectable: true,
        
    events: [
      //  { title: 'Event 1', date: '2024-08-06' },
      //  { title: 'Event 2', date: '2024-08-07' },
      
        {
            title: 'Indisponible',
            start: '2024-08-12T11:30:00',            
            end: '2024-08-14T10:30:00',
            backgroundColor: '#14B8A6',
            borderColor: '#14B8A6'
        },
        
        {
            title: 'Demande en attente',
            start: '2024-08-20T11:30:00',            
            end: '2024-08-23T10:30:00',
            backgroundColor: '#F5D300',
            borderColor: '#F5D300',
            textColor: '#000000'
        },

        { title: 'Maintenance',
            start: '2024-08-29',
            end: '2024-08-31',
            backgroundColor: '#F97316',
            borderColor: '#F97316'
        }
            
    ],
    displayEventTime: false,    
    // Empêche l'utilisateur de sélectionner les dates déjà prises
    selectOverlap: function(event: any) {
        return event.display === 'background';
    },
    // Grise les cases avant aujourd'hui et empêche l'utilisateur de choisir des dates passée
    validRange: function(nowDate: any) {
        return {start: nowDate}
    },
    select: function(selectInfo: any) {        
        console.log("Select Depart ",selectInfo.startStr)
        console.log(" Fin : ", selectInfo.endStr) // il ajoute un jour de plus ,donc faut retirer un jour lors de l'envoie
        console.log("selectInfo : ", selectInfo)
        selectedDate.value.dateStart = selectInfo.startStr
        selectedDate.value.dateEnd = pageUtils.substractOneDay(selectInfo.endStr)
        buttonOptions.value.isActive = true
    },
    // detecte si l'utilisateur enleve la sélection des cases 
    unselect: function(selectInfo: any) {            
       const clickedElement = selectInfo.jsEvent.target.id;
       const isResereButton = clickedElement === 'reserveButton'
       if (!isResereButton) {
        buttonOptions.value.isActive = false;
       }
    },
    buttonText: {
        month: 'Mois',
        year: 'Année',
        today: "Actuel"
    },    
    headerToolbar: {        
        left: 'prev,next,today',
        center: 'title',
        right: 'dayGridMonth,dayGridYear',                   
    }    
});

calendarOptions.value.events = reservationEvents as any;

</script>

<template>
    <ReservationModal :modal-options="optionModal" @close-modal="closeModal" @submit-button="submitBorrow">
        <p class="text-gray-600 mb-6">
            Vous avez sélectionné la période du
            <span class="font-semibold text-gray-800">{{ pageUtils.formatDateString(selectedDate.dateStart) }}</span>
            au
            <span class="font-semibold text-gray-800">{{ pageUtils.formatDateString(selectedDate.dateEnd) }}</span> .
        </p>
        <div>
            <p class="mb-2"><span class="block text-gray-600 font-semibold">Veuillez indiquer l'heure à laquelle vous souhaitez : </span></p>            
            <TimeInput :time-options="startTimeOption" v-model="startTimeOption.selectedTime"/> 
            <br><br>           
            <TimeInput :time-options="endTimeOptions" v-model="endTimeOptions.selectedTime"/>            
        </div>
    </ReservationModal>
    <div class="pt-0 pl-8 pr-8">
        <div class="flex flex-col 2xl:flex-row 2xl:space-x-4 justify-between ">
            <div class=" mt-6 order-last w-full 2xl:w-3/4 bg-white rounded font-opensans shadow-[0_.15rem_1.75rem_0_rgba(58,59,69,.15)] 2xl:mr-4">
                <div class="w-full space-y-0 p-4 rounded-t bg-slate-50">
                    <div class="w-full flex flex-row justify-between items-center">
                        <h1 class="uppercase text-blue-900 font-semibold tracking-wide text-sm mb-4">Calendrier de réservation</h1>                        
                    </div>
                    <div class="">
                        <FullCalendar :options="calendarOptions" class="calendar-container h-screen"/>
                        <div class="text-center pt-4">
                            <ActionButton :button-options="buttonOptions" @submit-button="openModal" id="reserveButton"/>                            
                        </div>
                    </div>
                </div>
            </div>   
            <div class="2xl:order-last 2xl:mt-2 w-full 2xl:w-1/4 2xl:pl-2">
                <div class=" bg-white rounded font-opensans shadow-[0_.15rem_1.75rem_0_rgba(58,59,69,.15)]">
                    <div class="w-full space-y-0 p-4 rounded-t bg-slate-50">
                        <div class="w-full flex flex-row justify-between items-center ">
                            <h1 class="uppercase text-blue-900 font-semibold tracking-wide text-sm mb-4">Détails de l'appareil</h1>
                        </div>
                        <DeviceCard :device-selected="deviceInformations"/>                                                         
                    </div>
                </div>                           
            </div>                                 
        </div>
    </div>               
</template>
<style scoped>
@media (min-width: 1536px) {
        .calendar-container {
            height: calc(100vh - 280px);
            overflow:auto;                                        
        }        
    }
</style>