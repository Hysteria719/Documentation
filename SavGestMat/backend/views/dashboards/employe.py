from rest_framework.viewsets import ReadOnlyModelViewSet

from django.db.models import Max
from gestmat.models import HistoriqueAppareil, Reservation
from gestmat.serializers import HistoriqueAppareilSerializer
from gestmat.permissions import IsEmployeAuthenticated

class HistoriqueAppareilView(ReadOnlyModelViewSet):

    serializer_class = HistoriqueAppareilSerializer
    #permission_classes = [IsEmployeAuthenticated]
    

    def get_queryset(self):                   
        userAuthenticated = self.request.user.id

        # Cette requête crée une liste de dictionnaires contenant l'ID de chaque appareil et la dernière date de son historique       
        historique = HistoriqueAppareil.objects.values('appareil_id').annotate(last=Max('cree_le'))      
        
        # Créer une liste de tuples (appareil_id, last) à partir des résultats de l'annotation
        histo_list = [(item['appareil_id'], item['last']) for item in historique]
        
        # Filtre les enregistrements pour obtenir les derniers enregistrements pour chaque appareil
        # Utilise l'ID des appareils et les dernières dates pour effectuer le filtrage
        queryset = HistoriqueAppareil.objects.filter(appareil_id__in=[item[0] for item in histo_list], cree_le__in=[item[1] for item in histo_list]).exclude(statut='detruit')
        reservation = Reservation.objects.values()

        statut = self.request.GET.get('statut')
        pagination = self.request.GET.get('pagination') 
        deviceId = self.request.GET.get('deviceId')       
        
        if pagination and pagination.lower() == 'none':            
            self.pagination_class = None

        if deviceId:
            queryset = queryset.filter(appareil_id=deviceId)   

        if statut == 'vosAppareils':
            #queryset = queryset.filter(statut='occupe',utilisateur_id=userAuthenticated) # à modifier
            reservation = reservation.filter(utilisateur_id=userAuthenticated).exclude(statut='refuse')
            queryset = queryset.filter(appareil_id__in=reservation.values('appareil_id'))

        elif statut == 'appEnAttente':
            queryset = queryset.filter(statut='occupe',utilisateur_id=userAuthenticated) # à modifier
        else :
            queryset = queryset.filter(statut='libre')    

        return queryset

