from rest_framework.serializers import ModelSerializer
from gestmat.models import Reservation

class ReservationEmployeSerializer(ModelSerializer):    

    class Meta:
        model= Reservation
        fields=['date_debut','date_fin','statut','appareil']

class ReservationDepartementSerializer(ModelSerializer):

    class Meta:
        model= Reservation
        fields='__all__'
