from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.shortcuts import get_object_or_404
from ..serializers import ModeloDisposivitoSerializer
from ..models import ModeloDisposivito  as dbModeloDisposivito


class ModeloDispositivosViews(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        elif self.request.method == 'POST':
            return [IsAdminUser()]
        elif self.request.method in ['PUT', 'DELETE']:
            return [IsAdminUser()]
        return super().get_permissions()
    def get(self,request):
        query_modeloDisposivo = dbModeloDisposivito.objects.all()
        Serializer =ModeloDisposivitoSerializer(query_modeloDisposivo,many=True)
        return Response(Serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = ModeloDisposivitoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Modelo Dispositivos criado com sucesso!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModeloDispositivoViews(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        elif self.request.method == 'POST':
            return [IsAdminUser()]
        elif self.request.method in ['PUT', 'DELETE']:
            return [IsAdminUser()]
        return super().get_permissions()
    
    def get(self,request,idKey):
        query_modeloDisposivo = get_object_or_404(dbModeloDisposivito,id=idKey)
        serializer = ModeloDisposivitoSerializer(query_modeloDisposivo,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,idKey):
        try:
            query_modeloDisposivo = dbModeloDisposivito.objects.get(id=idKey)
        except:
           return Response({'status': 'error', 'message': 'Modelo Dispositivos não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ModeloDisposivitoSerializer(dbModeloDisposivito,data = query_modeloDisposivo)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Modelo Dispositivos atualizado com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
  
    def delete(self,request,idKey):
        try:
            query_modeloDisposivo = dbModeloDisposivito.objects.get(id=idKey)
        except:
           return Response({'status': 'error', 'message': 'Modelo Dispositivos não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
       
        query_modeloDisposivo.delete()
        return Response({"message": "Modelo Dispositivos deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        