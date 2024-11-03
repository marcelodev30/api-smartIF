from rest_framework import serializers
from .models import Dispositivos,Sala,Setor,Usuario,ModeloDisposivito
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate


class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = ['nome']

class SalaSerializer(serializers.ModelSerializer):
    local = SetorSerializer()
    class Meta:
        model = Sala
        fields = ['nome','local']

class ModeloDisposivitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloDisposivito
        fields = ['nome','marca','modelo','min_temperatura','max_temperatura']

class DispositivoSerializer(serializers.ModelSerializer):
    modelo=ModeloDisposivitoSerializer()
    sala = SalaSerializer()
    class Meta:
        model = Dispositivos
        fields = ['id','modelo','status','sala']

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
    