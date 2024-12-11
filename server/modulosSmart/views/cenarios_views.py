from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.shortcuts import get_object_or_404
from ..serializers import RegistroCenárioSerializer,RegistroCenáriosSerializer
from ..models import Registro_Cenários as dbRegistro_Cenários


class CenariosViews(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        elif self.request.method == 'POST':
            return [IsAdminUser()]
        elif self.request.method in ['PUT', 'DELETE']:
            return [IsAdminUser()]
        return super().get_permissions()

    def get(self,request):
        query_cenarios= dbRegistro_Cenários.objects.all()
        serializer = RegistroCenáriosSerializer(query_cenarios,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = RegistroCenárioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Cenario criado com sucesso!"}, status=status.HTTP_201_CREATED)
        else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
class CenarioViews(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        elif self.request.method == 'POST':
            return [IsAdminUser()]
        elif self.request.method in ['PUT', 'DELETE']:
            return [IsAdminUser()]
        return super().get_permissions()

    def get(self,request,idKey):
        query_cemario = get_object_or_404(dbRegistro_Cenários,id=idKey)
        serializer = RegistroCenáriosSerializer(query_cemario,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,idKey):
        try:
            query_cemario = dbRegistro_Cenários.objects.get(id=idKey)
        except:
           return Response({'status': 'error', 'message': 'Cenario não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RegistroCenárioSerializer(dbRegistro_Cenários,data = query_cemario)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Cenario atualizado com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,idKey):
        try:
            query_cemario = dbRegistro_Cenários.objects.get(id=idKey)
        except:
           return Response({'status': 'error', 'message': 'Cenario não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        query_cemario.delete()
        return Response({"message": "Cenario deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)
