from django.db import models

class Tipo_user(models.Model):
    nome= models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Tipo de Usuario'

class Usuario(models.Model):
    login = models.CharField(max_length=50,unique=True)
    senha = models.CharField(max_length=255)
    nivel = models.ForeignKey(Tipo_user,on_delete=models.CASCADE) 
    nome = models.CharField(max_length=100)
   