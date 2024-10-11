from rest_framework import serializers
from .models import Dispositivos,Tipo,Sala,Setor


class TipoDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['nome']

class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = ['nome']

class SalaSerializer(serializers.ModelSerializer):
    local = SetorSerializer()
    class Meta:
        model = Sala
        fields = ['nome','local']

class DispositivoSerializer(serializers.ModelSerializer):
    tipo_id = TipoDispositivoSerializer()
    sala = SalaSerializer()
    class Meta:
        model = Dispositivos
        fields = ['id','tipo_id','marca','modelo','status','sala']