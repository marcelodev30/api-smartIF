from django.db import models

from Projetos.smartIF.server.arCondicionado.models import Sala

class Tipo(models.Model):
    nome= models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Dispositivo(models.Model):
    tipo_id = models.ForeignKey(Tipo,on_delete= models.CASCADE)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    sala = models.ForeignKey(Sala,on_delete=models.CASCADE)

class Comando(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    dispositivo = models.ForeignKey(Dispositivo,on_delete=models.CASCADE)

