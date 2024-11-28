from rest_framework import serializers
from ..models import ModeloDisposivito

    
class ModeloDisposivitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloDisposivito
        fields = ['id','nome','marca','modelo','min_temperatura','max_temperatura']
    
    def create(self, validated_data):
        modeloDisposivito = ModeloDisposivito.objects.create(
            nome=validated_data['nome'],
            marca=validated_data['marca'],
            modelo=validated_data['modelo'],
            min_temperatura=validated_data['min_temperatura'],
            max_temperatura=validated_data['max_temperatura'],
        )
        return modeloDisposivito
