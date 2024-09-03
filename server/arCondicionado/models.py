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
    def __str__(self):
        return self.host

class Modelo_Dispositivos(models.Model):
    TIPO_Dispositivos=[
        ('ArCondicionado','ArCondicionado'),
        ('Projetor','Projetor'),
        ('Televisão','Televisão')
    ]
    tipo = models.CharField(max_length=255,choices=TIPO_Dispositivos)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    codigo_IR = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.tipo} - {self.marca} - {self.modelo}'
   

class Dispositivos(models.Model):
    status = models.BooleanField(default=False)
    modelo_Dispositivos = models.ForeignKey(Modelo_Dispositivos,on_delete= models.CASCADE)
    def __str__(self):
        return f'{self.modelo_Dispositivos.tipo} - {self.modelo_Dispositivos.marca} - {self.modelo_Dispositivos.modelo}'

class Modulo_IF_Smart(models.Model):
    nome = models.CharField(max_length=255)
    temperatura = models.CharField(max_length=6)
    dispositivo = models.ManyToManyField(Dispositivos)
    serverMQTT = models.ForeignKey(ServerMQTT,on_delete= models.CASCADE)
    def __str__(self):
        return self.nome
    

class Sala(models.Model):
    Locais =[
        ('Bloco A','Bloca A'),
        ('Bloco B','Bloca B'),
        ('Bloco C','Bloca C'),
        ('Bloco Administrativo','Bloca Administrativo'),
    ]
    nome = models.CharField(max_length=255)
    local = models.CharField(max_length=255,choices=Locais)
    temperatura = models.CharField(max_length=6)
    modulo_IF_Smart = models.ManyToManyField(Modulo_IF_Smart)
    def __str__(self):
        return f'{self.nome} - {self.local}'