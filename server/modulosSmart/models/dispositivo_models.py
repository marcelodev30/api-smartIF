from django.db import models
from .salas_models import Sala
from uuid import uuid4


class ModeloDisposivito(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    nome = models.CharField(max_length=100,default='Ar Condicionado')
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    min_temperatura = models.IntegerField(default=18)
    max_temperatura = models.IntegerField(default=27)
    class Meta:
        verbose_name = 'Modelo do Disposivito'
    def __str__(self):
        return f'{self.nome} - {self.marca} - {self.modelo}'
    

class Dispositivos(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    modelo = models.ForeignKey(ModeloDisposivito,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    sala = models.ForeignKey(Sala,on_delete=models.CASCADE)
    updated= models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Disposivito'
    def __str__(self):
        return f'{self.modelo} - {self.sala.nome}'
 

class Comando(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    modelo = models.ForeignKey(ModeloDisposivito,on_delete=models.CASCADE)
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