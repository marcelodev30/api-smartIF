
from django.db import models
from uuid import uuid4
from .dispositivo_models import Dispositivos


TIPO_AÇÃO = [
    (True,'Ligar'),
    ( False,'Desligar')
]

TIPO_STATUS  = [
    (True,'Ativado'),
    ( False,'Desativado')
]

class Registro_Cenários(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    ação = models.BooleanField(choices=TIPO_AÇÃO)
    dispositivo = models.ForeignKey(Dispositivos,on_delete=models.SET_NULL ,null=True)
    data = models.DateTimeField()
    status = models.BooleanField(choices=TIPO_STATUS)
    class Meta:
        verbose_name = 'Registro de Cenário'