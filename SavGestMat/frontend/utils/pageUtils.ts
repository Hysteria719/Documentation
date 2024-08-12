
const formatDate = (date: Date | null) => {
    if (date) {
        const dateFormat: Date = new Date(date);
        const formatOptions: Intl.DateTimeFormatOptions = {
        dateStyle: 'medium'         
        }
        return dateFormat.toLocaleString(navigator.language, formatOptions);                  
    }                
    return null    
}
const formatDateString = (date: string | null) => {
    if (date) {
        const dateObj = new Date(date);
        const formatOptions: Intl.DateTimeFormatOptions = {
            dateStyle: 'medium'
        }
        return dateObj.toLocaleString(navigator.language, formatOptions)
    }
}
const substractOneDay = (date: string) => {
    const dateObj = new Date(date);

    // retire un jour
    dateObj.setDate(dateObj.getDate()-1);
    
    const year = dateObj.getFullYear();
    // +1 car compte le premier mois à 0
    const month = String(dateObj.getMonth() +1).padStart(2,'0')
    const day = String(dateObj.getDate()).padStart(2,'0')

    return `${year}-${month}-${day}`
}



export const pageUtils = {
    formatDate,
    formatDateString,
    substractOneDay    
}