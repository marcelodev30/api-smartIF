#from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import Usuario as User
from ..serializers import UsuarioSerializer,UsuarioDetalhesSerializer


class UsuárioViews(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAdminUser()]
        elif self.request.method == 'POST':
            return [AllowAny()]
        return super().get_permissions()
 
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuário criado com sucesso!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        try:
            query_usuario = User.objects.all()
        except:
            return Response({'status': 'error', 'message': 'Usuario não encontrado!'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = UsuarioDetalhesSerializer(query_usuario,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 

class UsuárioNívelAcessoViews(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request,idKey):
        try:
            query_usuario = User.objects.get(id=idKey)
        except:
             return Response({'status': 'error', 'message': 'Usuario não encontrado!'}, status=status.HTTP_404_NOT_FOUND) 

        if query_usuario.is_staff:
            query_usuario.is_staff = False 
            query_usuario.save()
        else: 
            query_usuario.is_staff= True
            query_usuario.save()
        return Response({"message": "Nível de acesso atualizado com sucesso."}, status=status.HTTP_200_OK)
    
    
class UsuárioDetalhesViews(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        elif self.request.method in ['PUT', 'DELETE']:
            return [IsAdminUser()]
        return super().get_permissions()

    def get(self,request,idKey):
        try:
            query_usuario = User.objects.get(id=idKey)
        except:
            return Response({'status': 'error', 'message': 'Usuario não encontrado!'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = UsuarioDetalhesSerializer(query_usuario)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,idKey):
        try:
            query_usuario = User.objects.get(id=idKey)
        except:
            return Response({'status': 'error', 'message': 'Usuario não encontrado!'},status=status.HTTP_404_NOT_FOUND)

        serializer = UsuarioDetalhesSerializer(User,data=query_usuario)
        if serializer.is_valid:
            serializer.save()
            return Response({"message": "Usuário atualizado com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,idKey):
        try:
            query_usuario = User.objects.get(id=idKey)
        except:
            return Response({'status': 'error', 'message': 'Usuario não encontrado!'},status=status.HTTP_404_NOT_FOUND)
        query_usuario.delete()
        return Response({"message": "Usuário deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)