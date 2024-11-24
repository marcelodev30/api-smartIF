from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Dispositivos,Sala,Setor,ModeloDisposivito,Registro_Cenários


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
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
        )
        return 

class UsuarioDetalhesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')

class RegistroCenáriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro_Cenários
        fields = ["nome","ação","dispositivo","data","status"]