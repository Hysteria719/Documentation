import router from "@/router";

// Redirection en fonction du rôle de l'utilisateur.
export function redirectBasedOnRole(userRole: string | null): void {    
    switch (userRole) {
        case 'employe':
            router.push('employe/dashboard');            
            break;
        case 'admin':
            router.push('admin/dashboard');

            break;
        default:
            router.push('/');
            break;
    }
}