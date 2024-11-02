from django.db import models
from uuid import uuid4

class RegistroLog(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    comando = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    dispositivo = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Registro de Log'
