from django.db import models

class Setor(models.Model):
    nome= models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Sala(models.Model):
    nome = models.CharField(max_length=100)
    local = models.ForeignKey(Setor,on_delete= models.CASCADE)
    def __str__(self):
        return f' ${self.nome}'

class Registro_Uso(models.Model):
    comeco = models.DateTimeField()
    fim = models.DateTimeField()
    sala = models.ForeignKey(Sala,on_delete=models.CASCADE)