from django.urls import path
from .views import DispositivoSendMQTT

urlpatterns = [
    path('api/Dispositivos/send', DispositivoSendMQTT.as_view(), name='send'),
]