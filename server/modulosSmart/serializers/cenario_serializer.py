from rest_framework import serializers
from ..models import Dispositivos,Sala,Setor,ModeloDisposivito,Registro_Cenários


class _ModeloDisposivitosSerializer_Cenários(serializers.ModelSerializer):
    class Meta:
        model = ModeloDisposivito
        fields = ['nome','marca','modelo']

class _SetorSerializer_Dispositivo(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = ['nome']

class _SalasSerializera_Dispositivo(serializers.ModelSerializer):
    local = _SetorSerializer_Dispositivo()
    class Meta:
        model = Sala
        fields = ['nome','local']

class _DispositivosSerializer_Cenários(serializers.ModelSerializer):
    modelo= _ModeloDisposivitosSerializer_Cenários()
    sala =  _SalasSerializera_Dispositivo()
    class Meta:
        model = Dispositivos
        fields = ['id','modelo','sala']


class RegistroCenárioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro_Cenários
        fields = ["id","ação","dispositivo","data","status"]

class RegistroCenáriosSerializer(serializers.ModelSerializer):
    dispositivo = _DispositivosSerializer_Cenários()
    class Meta:
        model = Registro_Cenários
        fields = ["id","ação","data","status","dispositivo"]

