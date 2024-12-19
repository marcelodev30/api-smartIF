from .mqtt_client import client
from .models import Comando as dbComando
from .models import Dispositivos
from .models import RegistroLog

def send_mqtt(dispositivo_id ,ação:bool):
    query_Dispositivo = Dispositivos.objects.get(id= dispositivo_id)
    if ação:
        Comando = 'on'
        query_Dispositivo.status= True
        query_Dispositivo.save()
    else:
       Comando = 'off'
       query_Dispositivo.status= False
       query_Dispositivo.save()
    query_dbComando = dbComando.objects.get(nome=Comando, modelo = query_Dispositivo.modelo.id)
    RegistroLog(comando = Comando,usuario='Cenario User',dispositivo = query_Dispositivo.modelo.nome+" - "+query_Dispositivo.sala.nome).save()
    client.publish('smartIF/dispositivo/'+str(dispositivo_id), query_dbComando.codigo, qos=1) 
