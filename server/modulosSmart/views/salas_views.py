from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from ..serializers import SalasSerializer,SalaSerializer
from ..models import Sala as dbSala


class SalasViews(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        query_sala = dbSala.objects.all()
        serializer = SalasSerializer(query_sala,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = SalaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Sala ou Laboratório criado com sucesso!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SalaViews(APIView):
    permission_classes = [IsAdminUser]
    def get(selt,request,idKey):
        query_sala = get_object_or_404(dbSala,id=idKey)
        serializer = SalasSerializer(query_sala,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,idKey):
        try:
            query_sala = dbSala.objects.get(id=idKey)
        except:
           return Response({'status': 'error', 'message': 'Sala ou Laboratório não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SalaSerializer(dbSala,data = query_sala)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Sala ou Laboratório atualizado com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
            
  
    def delete(self,request,idKey):
        try:
            query_sala = dbSala.objects.get(id=idKey)
        except:
           return Response({'status': 'error', 'message': 'Sala ou Laboratório não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
       
        query_sala.delete()
        return Response({"message": "Sala ou Laboratório deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)