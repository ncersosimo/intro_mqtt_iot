# Ejemplos de clase

En esta práctica utilizaremos la librería de python "Paho MQTT" para enviar mensajes

Logearse desde VM e instalar pahoo-mqtt para python:
```sh
$ python3 -m pip install paho-mqtt
```

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

Crear la carpeta "clase_2" para trabajar sobre los ejemplos de esta clase.
```sh
$ mkdir clase_2
```

Abrir el Visual Studio Code y conectarse de forma remota al dispositivo. Trabajaremos sobre la carpeta recientemente creada.


### 1 - El publicador
Desde el VSC crear un script de python el cual llamaremos "publicador.py". Comenzar por instanciar las librerías que utilizaremos en este ejemplo:
```python
import time
import paho.mqtt.client as paho
```

Crear las siguientes variables globales que utilizaremos como definiciones en el resto del código:
```python
broker = "localhost"
port = 1883
topico = "sensor/prueba/1"
```

Crear la función de "on_connect" que utilizaremos para verificar que nuestro script pude conectarse exitosamente a la aplicación:
```python
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt Publicador conectado")
    else:
        print(f"Mqtt Publicador connection faild, error code={rc}")
```

Crear el cliente MQTT y conectarse la IP y puerto definidos:
```python
client = paho.Client("publicador")
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()
```

Crear un loop para enviar un mensaje de forma constante una cierta cantidad de veces, por ejemplo:
```python
for i in range(40):
    ret = client.publish(topico, i) 
    time.sleep(2)
```

Finalizar el script con la desconexión del publicador y la finalización del cliente MQTT:
```python
client.disconnect()
client.loop_stop()
```

### 2 - El suscriptor
Desde el VSC crear un script de python el cual llamaremos "suscriptor.py". Comenzar por instanciar las librerías que utilizaremos en este ejemplo:
```python
import paho.mqtt.client as paho
```

Crear las siguientes variables globales que utilizaremos como definiciones en el resto del código:
```python
broker = "localhost"
port = 1883
topico = "sensor/prueba/1"
```

Crear la función de "on_connect" que utilizaremos para verificar que nuestro script pude conectarse exitosamente a la aplicación:
```python
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt Publicador conectado")
        client.subscribe(topico)
    else:
        print(f"Mqtt Publicador connection faild, error code={rc}")
```

Crear la función de "on_message" que utilizaremos para capturar los mensajes que llegan a los topicos suscriptos:
```python
def on_message(client, userdata, message):
    topico = message.topic
    mensaje = str(message.payload.decode("utf-8"))
    print(f"mensaje recibido {mensaje} en topico {topico}")
```

Crear el cliente MQTT y conectarse la IP y puerto definidos:
```python
client = paho.Client("suscriptor")
client.on_message = on_message
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()
```

Crear un loop para que el script no finalice y quede esperando por mensajes MQTT
```python
while True:    
    pass
```

Mencionar que en este momento existen dos "procesos" ejecutandose en nuestro script:
- Por un lado la función de "on_message" que es invocada cada vez que llega un mensaje nuevo por MQTT.
- Por otro lado el loop principal del programa (while True) que en este momento no está realizando ninguna acción.

Veremos en clases más adelantes como es que esto funciona y como sacarle más provecho en el futuro.
