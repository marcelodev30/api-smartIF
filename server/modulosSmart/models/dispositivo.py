from django.db import models

from .salas import Sala

class Tipo(models.Model):
    nome= models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Dispositivos(models.Model):
    tipo_id = models.ForeignKey(Tipo,on_delete= models.CASCADE)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    sala = models.ForeignKey(Sala,on_delete=models.CASCADE)

class Comando(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    dispositivo = models.ForeignKey(Dispositivos,on_delete=models.CASCADE)

class modulo_smart(models.Model):
    nome = models.CharField(max_length=200)
    dispositivo = models.ManyToManyField(Dispositivos)