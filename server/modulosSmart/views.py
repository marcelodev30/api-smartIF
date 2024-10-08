from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Comando as dbComando

class DispositivoSendMQTT(APIView):
    def post(self, request):
        id = request.data.get('id')
        Comando = request.data.get('Comando')
        dados = dbComando.objects.filter(nome=Comando,dispositivo=id).values_list('codigo',flat=True)
        return Response({'status': 'success', 'Comando': f'{str(dados).split("'")[1]}'}, status=status.HTTP_200_OK)