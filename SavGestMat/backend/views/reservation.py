from rest_framework.viewsets import ReadOnlyModelViewSet

from gestmat.models import Reservation
from gestmat.serializers import ReservationEmployeSerializer
from gestmat.permissions import IsEmployeAuthenticated

class ReservationEmployeView(ReadOnlyModelViewSet):

    serializer_class = ReservationEmployeSerializer
    permission_classes = [IsEmployeAuthenticated]

    def get_queryset(self):
        self.pagination_class = None
        deviceId = self.request.GET.get('deviceId')        
        queryset = Reservation.objects.filter(appareil_id=deviceId).exclude(statut='refuse')        
            
        return queryset
        
            


