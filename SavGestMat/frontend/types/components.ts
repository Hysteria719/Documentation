interface ButtonAction {
    title: string;    
    isActive: boolean;
}
interface TimeOption {
    id: string;
    name: string;    
    selectedTime: string;
    label: string
}
interface ModalOption {
    isVisible: boolean;
    title: string;
    submitButtonText?: string;
    closeButtonText: string;
}

export type {ButtonAction, TimeOption, ModalOption}