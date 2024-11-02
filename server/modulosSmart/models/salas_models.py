from django.db import models
from uuid import uuid4
class Setor(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    nome= models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Setor'

class Sala(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    nome = models.CharField(max_length=100)
    local = models.ForeignKey(Setor,on_delete= models.CASCADE)
    def __str__(self):
        return f' ${self.nome}'
    class Meta:
        verbose_name = 'Salas - Laboratorio'
    

class Registro_Uso(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    comeco = models.DateTimeField()
    fim = models.DateTimeField()
    sala = models.ForeignKey(Sala,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Registro Uso'