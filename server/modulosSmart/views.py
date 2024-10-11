from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comando as dbComando
from .models import Dispositivos as dbDispositivos
from .serializers import DispositivoSerializer

class DispositivoSendMQTT(APIView):
    def post(self, request):

        request_id = request.data.get('id')
        request_Comando = request.data.get('Comando')
        query_dados = dbComando.objects.filter(nome = request_Comando, dispositivo = request_id)

        if(query_dados.exists()):
            dado = str(query_dados.values_list('codigo',flat=True)).split("'")[1]
            return Response({'status': 'success', 'Comando': f'{dado}'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error'}, status=status.HTTP_404_NOT_FOUND)

class GetDispositivos(APIView):
    def get(self, request):
        query_dados = dbDispositivos.objects.all()
        serializer = DispositivoSerializer(query_dados, many=True)
        return Response(serializer.data)