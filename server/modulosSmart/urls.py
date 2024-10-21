from django.urls import path
from .views import DispositivoSendMQTT,GetDispositivos
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('api/Dispositivos/send', DispositivoSendMQTT.as_view(), name='send'),
    path('api/Dispositivos', GetDispositivos.as_view(), name='getData'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]