from rest_framework import serializers
from ..models import Dispositivos,Sala,Setor,ModeloDisposivito


class _ModeloDisposivitosSerializer_Dispositivo(serializers.ModelSerializer):
    class Meta:
        model = ModeloDisposivito
        fields = ['nome','marca','modelo','min_temperatura','max_temperatura']

class _SetorSerializer_Dispositivo(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = ['nome']

class _SalasSerializera_Dispositivo(serializers.ModelSerializer):
    local = _SetorSerializer_Dispositivo()
    class Meta:
        model = Sala
        fields = ['nome','local']

class DispositivosSerializer(serializers.ModelSerializer):
    modelo= _ModeloDisposivitosSerializer_Dispositivo()
    sala =  _SalasSerializera_Dispositivo()
    class Meta:
        model = Dispositivos
        fields = ['id','modelo','status','atual_temperatura','sala']


class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivos
        fields = ['modelo','status','sala']
    def create(self, validated_data):
        dispositivo = Dispositivos.objects.create(
            modelo=validated_data['modelo'],
            sala=validated_data['sala'],
        )
        return dispositivo

