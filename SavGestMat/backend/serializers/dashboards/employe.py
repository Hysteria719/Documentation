from rest_framework.serializers import ModelSerializer
from gestmat.models import Appareil, HistoriqueAppareil

class AppareilBaseSerializer(ModelSerializer):

    class Meta:
        model=Appareil
        fields = '__all__'

class HistoriqueAppareilSerializer(ModelSerializer):

    appareil = AppareilBaseSerializer()

    class Meta:
        model = HistoriqueAppareil       
        fields = ['id','cree_le','statut','appareil_id','utilisateur_id', 'appareil']