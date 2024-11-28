from rest_framework import serializers
from ..models import Sala
from .setor_serializer import SetorSerializer


class SalasSerializer(serializers.ModelSerializer):
    local = SetorSerializer()
    class Meta:
        model = Sala
        fields = ['id','nome','local']

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = ['nome','local']
    
    def create(self, validated_data):
        sala = Sala.objects.create(
            nome=validated_data['nome'],
            local=validated_data['local'],
        )
        return sala
