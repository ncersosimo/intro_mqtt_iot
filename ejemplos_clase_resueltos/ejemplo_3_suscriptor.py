import paho.mqtt.client as paho

# instalar paho con:
# $ python3 -m pip install paho-mqtt

broker = "localhost"
port = 1883
topico = "sensor/prueba/1"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt Publicador conectado")
        # El sistema debe suscribirse a los topicos en este lugar
        # por si llega a desconectarse y reconectarse debe volver
        # a suscribirse a los topicos
        # Podria definirse una lista de topicos y suscribirse a todos
        # con un bucle
        client.subscribe(topico)
    else:
        print(f"Mqtt Publicador connection faild, error code={rc}")


def on_message(client, userdata, message):
    topico = message.topic
    mensaje = str(message.payload.decode("utf-8"))
    print(f"mensaje recibido {mensaje} en topico {topico}")


client = paho.Client("suscriptor")
client.on_message = on_message
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()

# El programa principal no hace más nada
# Solo se recibiran mensajes en on_message
# El "while True" es para evitar que el programa termine
while True:    
    pass
