from django.urls import path
from .views import DispositivoControleTemperatura,DispositivosViews,DispositivoControleEstado,DispositivoViews
from .views import UsuárioNívelAcessoViews,UsuárioDetalhesViews,UsuárioViews
from .views import ModeloDispositivosViews,ModeloDispositivoViews
from .views import CenariosViews,CenarioViews
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/dispositivos', DispositivosViews.as_view(), name='getData'),
    path('api/dispositivo/<uuid:idKey>', DispositivoViews.as_view(), name='getData'),
    path('api/dispositivo/controle/temperatura', DispositivoControleTemperatura.as_view(), name='send'),
    path('api/dispositivo/controle/estado', DispositivoControleEstado.as_view(), name='controleState'),
    path('api/dispositivos/modelo_dispositivos', ModeloDispositivosViews.as_view(), name='get_modelo_dispositivos'),
    path('api/dispositivo/modelo_dispositivo/<uuid:idKey>', ModeloDispositivoViews.as_view(), name='get_modelo_dispositivo'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/usuarios/', UsuárioViews.as_view(), name='user'),
    path('api/usuario/<int:idKey>/', UsuárioDetalhesViews.as_view(), name='usuario-detalhes'),
    path('api/usuarios/nivel-acesso/<uuid:idKey>', UsuárioNívelAcessoViews.as_view(), name='usuario_nivel'),
    path('api/Cenarios/', CenariosViews.as_view(), name='get_Cenarios'),
    path('api/Cenario/<uuid:idKey>', CenarioViews.as_view(), name='get_Cenario'),
   
]