from rest_framework import serializers
from ..models import Setor

class SetorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = ['id','nome']
    

class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = ['nome']
    
    def create(self, validated_data):
        setor = Setor.objects.create(
            nome=validated_data['nome'],
        )
        return setor

