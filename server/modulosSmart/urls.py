from django.urls import path
from .views import DispositivoControleTemperatura,GetDispositivos,CreateUserViews,DispositivoControleEstado,DispositivoDetailAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/dispositivos', GetDispositivos.as_view(), name='getData'),
    path('api/dispositivos/<uuid:idKey>/', DispositivoDetailAPI.as_view(), name='getData'),
    path('api/dispositivos/controle/temperatura', DispositivoControleTemperatura.as_view(), name='send'),
    path('api/dispositivo/controle/estado', DispositivoControleEstado.as_view(), name='controleState'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/user/', CreateUserViews.as_view(), name='user'),
   
]