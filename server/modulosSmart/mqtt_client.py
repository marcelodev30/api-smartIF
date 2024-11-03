
import paho.mqtt.client as mqtt
from django.conf import settings


mqtt_topic = 'smartIF/modulo_smart/status'

def on_connect(client, userdata, flags, rc):
    if(rc == 0):
        client.subscribe(mqtt_topic)
        print("Conectado ao broker MQTT")
    else:
        print("Failed to connect, return code %d\n",rc)
   
def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,settings.ID_CLIENT_MQTT)
except:
    client = mqtt.Client(settings.ID_CLIENT_MQTT)


client.username_pw_set(settings.MQTT_USER,settings.MQTT_PASSWORD)
client.on_connect = on_connect
client.on_message = on_message
client.connect(settings.MQTT_BROKER , 1883)
client.loop_start()
