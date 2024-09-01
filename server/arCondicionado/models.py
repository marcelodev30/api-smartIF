from django.db import models


class Usuario(models.Model):
    TIPO_USER=[
        ('Professor','Professor'),
        ('Coordenação de turma','Coordenação de turma')
    ]
    login = models.CharField(max_length=50)
    senha = models.CharField(max_length=255)
    nivel = models.CharField(max_length=30,choices=TIPO_USER,default=TIPO_USER[1]) 
    img_url = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)
   

class ServerMQTT(models.Model):
    usuario = models.CharField(max_length=50)  
    senha = models.CharField(max_length=255)
    host = models.CharField(max_length=13)

class Dispositivos(models.Model):
    nome = models.CharField(max_length=255)
    codigo_ir = models.CharField(max_length=20)
    temperatura = models.CharField(max_length=6)
    status = models.BooleanField()
    serverMQTT = models.ForeignKey(ServerMQTT)

class Sala(models.Model):
    nome = models.CharField(max_length=255)
    temperatura = models.CharField(max_length=6)
    dispositivo = models.ForeignKey(Dispositivos)