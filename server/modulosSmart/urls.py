from django.urls import path
from .views import DispositivoControleTemperatura,Dispositivos,UsuárioViews,DispositivoControleEstado,Dispositivo,UsuárioNívelAcesso,UsuárioDetalhes
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/dispositivos', Dispositivos.as_view(), name='getData'),
    path('api/dispositivos/<uuid:idKey>', Dispositivo.as_view(), name='getData'),
    path('api/dispositivos/controle/temperatura', DispositivoControleTemperatura.as_view(), name='send'),
    path('api/dispositivo/controle/estado', DispositivoControleEstado.as_view(), name='controleState'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/usuarios/', UsuárioViews.as_view(), name='user'),
    path('api/usuarios/<int:idKey>/', UsuárioDetalhes.as_view(), name='usuario-detalhes'),
    path('api/usuarios/nivel-acesso/<uuid:idKey>', UsuárioNívelAcesso.as_view(), name='usuario_nivel'),
   
]