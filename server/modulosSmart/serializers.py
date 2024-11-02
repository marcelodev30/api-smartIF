from rest_framework import serializers
from .models import Dispositivos,Tipo,Sala,Setor,Usuario
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate


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

class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)
    class Meta:
        model = Usuario
        fields = ['login','senha','nome']
    def create(self,validated_data):
        user  = Usuario(
            login = validated_data['login'],
            nome = validated_data['nome'],
            senha=validated_data['senha']
            )
        #user.senha=make_password(validated_data['senha'])
        user.save()
        return user 
    