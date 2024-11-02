from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from ..serializers import UsuarioSerializer
from ..models import Usuario as userDB



class CreateUserViews(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UsuarioSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'name':str(user.nome)
        }, status=status.HTTP_201_CREATED)


class loginViews(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        request_login = request.data.get('login')
        request_senha = request.data.get('senha')
        query_user = userDB.objects.filter(login=request_login,senha=request_senha)
        if(query_user.exists()):
            refresh = RefreshToken.for_user(userDB)
            return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

     
            