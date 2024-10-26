
import paho.mqtt.client as mqtt
from django.conf import settings

client_id = f'server-mqttt'

def on_connect(client, userdata, flags, rc):
    if(rc == 0):
        print("Conectado ao broker MQTT")
    else:
        print("Failed to connect, return code %d\n",rc)
   
try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,client_id)
except:
    client = mqtt.Client(client_id)

client.username_pw_set('marcelomqtt','marcelo@ash')
client.on_connect = on_connect
client.connect("192.168.0.115", 1883)
client.loop_start()
