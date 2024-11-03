from django.db import models
from uuid import uuid4

class Tipo_user(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    nome= models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Tipo de Usuario'

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    login = models.CharField(max_length=50,unique=True)
    senha = models.CharField(max_length=255)
    nivel = models.ForeignKey(Tipo_user,on_delete=models.CASCADE,default=1) 
    nome = models.CharField(max_length=100)
   