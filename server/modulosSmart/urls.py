from django.urls import path
from .views import DispositivoSendMQTT,GetDispositivos,CreateUserViews,loginViews
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/Dispositivos/send', DispositivoSendMQTT.as_view(), name='send'),
    path('api/Dispositivos', GetDispositivos.as_view(), name='getData'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/user/', CreateUserViews.as_view(), name='user'),
    path('api/login/login', loginViews.as_view(), name='user'),
]