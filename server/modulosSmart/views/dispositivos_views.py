from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Comando as dbComando
from ..models import Dispositivos as dbDispositivos
from ..models import RegistroLog
from ..serializers import DispositivoSerializer
from ..mqtt_client import client

class DispositivoSendMQTT(APIView):
    def post(self, request):

        request_id = request.data.get('id')
        request_Comando = request.data.get('Comando')
        
        query_Dispositivo = dbDispositivos.objects.get(id= request_id)        
        query_dados = dbComando.objects.filter(nome = request_Comando, modelo = query_Dispositivo.modelo.id)
      
        if(query_dados.exists()):
            dado = str(query_dados.values_list('codigo',flat=True)).split("'")[1]
            client.publish('smartIF/dispositivo/'+str(request_id),dado)

            RegistroLog(comando = request_Comando,usuario=request.user.username,dispositivo = query_Dispositivo.modelo.nome+" - "+query_Dispositivo.sala.nome).save()
            if request_Comando == 'on':
                query_Dispositivo.status=True
                query_Dispositivo.save()
            elif request_Comando =='off':
               query_Dispositivo.status= False
               query_Dispositivo.save()
            
            
            return Response({'status': 'success', 'Comando': f'{dado}'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error'}, status=status.HTTP_404_NOT_FOUND)

class GetDispositivos(APIView):
    def get(self, request):
        query_dados = dbDispositivos.objects.all()
        serializer = DispositivoSerializer(query_dados, many=True)
        return Response(serializer.data)