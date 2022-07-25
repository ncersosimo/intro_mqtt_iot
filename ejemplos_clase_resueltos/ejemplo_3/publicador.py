import time
import paho.mqtt.client as paho

# instalar paho con:
# $ python3 -m pip install paho-mqtt

broker = "localhost"
port = 1883
topico = "sensor/prueba/1"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt Publicador conectado")
    else:
        print(f"Mqtt Publicador connection faild, error code={rc}")

client = paho.Client("publicador")
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()

for i in range(40):
    ret = client.publish(topico, i) 
    time.sleep(2)

client.disconnect()
client.loop_stop()
