from django.urls import path
from .views import DispositivoSendMQTT,GetDispositivos

urlpatterns = [
    path('api/Dispositivos/send', DispositivoSendMQTT.as_view(), name='send'),
    path('api/Dispositivos', GetDispositivos.as_view(), name='getData'),
]