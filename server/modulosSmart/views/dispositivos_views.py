from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Comando as dbComando
from ..models import Dispositivos as dbDispositivos
from ..models import RegistroLog
from ..serializers import DispositivosSerializer,DispositivoSerializer
from ..mqtt_client import client
from rest_framework.permissions import AllowAny,IsAdminUser


class DispositivosViews(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        query_dados = dbDispositivos.objects.all()
        serializer = DispositivosSerializer(query_dados, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
  
    def post(self,request):
        serializer = DispositivoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Dispositivo criado com sucesso!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DispositivoViews(APIView):
    permission_classes = [IsAdminUser]
    def get(selt,request,idKey):
        query_dispositivo = get_object_or_404(dbDispositivos,id=idKey)
        serializer = DispositivosSerializer(query_dispositivo,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,idKey):
        try:
            query_dispositivo = dbDispositivos.objects.get(id=idKey)
        except:
           return Response({'status': 'error', 'message': 'Dispositivo não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DispositivoSerializer(dbDispositivos,data = query_dispositivo)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Dispositivo atualizado com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
            
  
    def delete(self,request,idKey):
        try:
            query_dispositivo = dbDispositivos.objects.get(id=idKey)
        except:
           return Response({'status': 'error', 'message': 'Dispositivo não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
       
        query_dispositivo.delete()
        return Response({"message": "Dispositivo deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)


class DispositivoControleTemperatura(APIView):
    permission_classes = [AllowAny]
    def post(self, request):

        request_id = request.data.get('id')
        request_Comando = request.data.get('Comando')
        try:
            query_Dispositivo = dbDispositivos.objects.get(id= request_id)
        except:
            return Response({'status': 'error', 'message': 'Dispositivo não encontrado!'}, status=status.HTTP_404_NOT_FOUND) 

        try:
            temperatura_comando = int(request_Comando)
            if (temperatura_comando >= query_Dispositivo.modelo.min_temperatura and temperatura_comando <= query_Dispositivo.modelo.max_temperatura):  
                try:
                    query_dbComando = dbComando.objects.get(nome = request_Comando, modelo = query_Dispositivo.modelo.id)
                except:
                    return Response({'status': 'error', 'message': 'Comando não foi cadastrado no banco de dados!'}, status=status.HTTP_404_NOT_FOUND)
                if(query_Dispositivo.status):
                    client.publish('smartIF/dispositivo/'+str(request_id),query_dbComando.codigo)
                    query_Dispositivo.atual_temperatura = temperatura_comando
                    RegistroLog(comando = request_Comando,usuario=request.user.username,dispositivo = query_Dispositivo.modelo.nome+" - "+query_Dispositivo.sala.nome).save()
                    return Response({'status': 'success', 'message': f"O ar-condicionado do {query_Dispositivo.sala.nome} está com a temperatura ajustada para {temperatura_comando}°C"}, status=status.HTTP_200_OK)
                else:
                     return Response({'status': 'error', 'message': 'Dispositivo está desligado!'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'status': 'error', 'message': 'Temperatura fora do intervalo permitido!'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
                return Response({'status': 'error', 'message': 'Comando não representa uma temperatura válida!'}, status=status.HTTP_400_BAD_REQUEST)


class DispositivoControleEstado(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        request_id = request.data.get('id')
        try:
            query_Dispositivo = dbDispositivos.objects.get(id= request_id)
        except:
            return Response({'status': 'error', 'message': 'Dispositivo não encontrado!'}, status=status.HTTP_404_NOT_FOUND) 

        if(query_Dispositivo.status):
            if query_Dispositivo.atual_temperatura!=22:query_Dispositivo.atual_temperatura=22
            query_Dispositivo.status=False
            request_Comando = 'off'
            query_Dispositivo.save()
        else:
            query_Dispositivo.status=True
            request_Comando = 'on'
            query_Dispositivo.save()
          

        query_dbComando = dbComando.objects.get(nome = request_Comando, modelo = query_Dispositivo.modelo.id)
        client.publish('smartIF/dispositivo/'+str(request_id),query_dbComando.codigo)
        RegistroLog(comando = request_Comando,usuario=request.user.username,dispositivo = query_Dispositivo.modelo.nome+" - "+query_Dispositivo.sala.nome).save()
        
        return Response({'status': 'success', 'message': f"O ar-condicionado do {query_Dispositivo.sala.nome} foi {query_Dispositivo.status if 'Ligado' else 'Desligado'} com sucesso"}, status=status.HTTP_200_OK)

   
       
    
         