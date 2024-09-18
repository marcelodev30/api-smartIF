from django.db import models

class Usuario(models.Model):
    TIPO_USER=[
        ('Professor','Professor'),
        ('Coordenação de turma','Coordenação de turma')
    ]
    login = models.CharField(max_length=50,unique=True)
    senha = models.CharField(max_length=255)
    nivel = models.CharField(max_length=30,choices=TIPO_USER,default=TIPO_USER[1]) 
    nome = models.CharField(max_length=100)
   