#from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import Usuario 


class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ('email', 'password','nome')

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            password=validated_data['password'],
            email=validated_data.get('email'),
            nome=validated_data.get('nome'),
        )
        return user

class UsuarioDetalhesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','email', 'nome')