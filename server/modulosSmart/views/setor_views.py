from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.shortcuts import get_object_or_404
from ..serializers import SetorSerializer,SetorsSerializer
from ..models import Setor  as dbSetor

class SetorsViews(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        elif self.request.method == 'POST':
            return [IsAdminUser()]
        elif self.request.method in ['PUT', 'DELETE']:
            return [IsAdminUser()]
        return super().get_permissions()
    def get(self,request):
        query_setors = dbSetor.objects.all()
        Serializer = SetorsSerializer(query_setors,many=True)
        return Response(Serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = SetorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Setor criado com sucesso!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SetorViews(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        elif self.request.method == 'POST':
            return [IsAdminUser()]
        elif self.request.method in ['PUT', 'DELETE']:
            return [IsAdminUser()]
        return super().get_permissions()
    
    def get(self,request,idKey):
        query_setor = get_object_or_404(dbSetor,id=idKey)
        serializer = SetorsSerializer(query_setor,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,idKey):
        try:
            query_setor = dbSetor.objects.get(id=idKey)
        except:
           return Response({'status': 'error', 'message': 'Setor não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SetorSerializer(dbSetor,data = query_setor)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Setor atualizado com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
  
    def delete(self,request,idKey):
        try:
            query_setor = dbSetor.objects.get(id=idKey)
        except:
           return Response({'status': 'error', 'message': 'Setor não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
       
        query_setor.delete()
        return Response({"message": "Setor deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        