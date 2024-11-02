from django.db import models
from .salas_models import Sala
from uuid import uuid4


class Tipo(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    nome= models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Tipo do Dispositivo'

class Dispositivos(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    tipo_id = models.ForeignKey(Tipo,on_delete= models.CASCADE)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    sala = models.ForeignKey(Sala,on_delete=models.CASCADE)
    updated= models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.tipo_id.nome} - {self.sala.nome} - {self.marca} - {self.modelo}'
 

class Comando(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    dispositivo = models.ForeignKey(Dispositivos,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Comandos IR'

class modulo_smart(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    nome = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    temperatura = models.FloatField()
    dispositivo = models.ManyToManyField(Dispositivos)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Modulo Smart IF'