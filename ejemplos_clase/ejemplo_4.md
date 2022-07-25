# Ejemplos de clase

En esta práctica utilizaremos el simulador de drone "drone emulado" junto a la librería de Paho MQTT

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

Abrir el Visual Studio Code y conectarse de forma remota al dispositivo. Trabajaremos sobre la carpeta recientemente creada para esta clase. Copiar allí el script "controlador.py" disponible en la carpeta de ejemplos de clase.

Desde ssh conectado a la VM, en la carpeta "repos" clonar el repositorio del simulador de drone:
```sh
$ git clone https://github.com/InoveAlumnos/drone_emulado_iot
```

Topicos que soporta este mock drone emulado:
|             |          |      | datos ejemplo
| ----------  | -------- | -----| -----
|  actuadores | luces    | 1    |  0/1
|  actuadores | volar    |      |  0/1


### 1 - Lanzar el simulador drone emulado
Desde ssh conectado a la VM, ingresar a la carpeta clonada del "drone_emulado" y lanzar la aplicación:
```sh
$ python3 app.py
```

Ingresar a su explorador web e ingresar a al aplicación del drone:
```
http://<ip_VM>:5009
```

### 2 - Ensayar que el simulador funcione
Utilizar MQTTExplorer o mosquitto_pub para enviar mensajes a los tipos disponibles en este simulador, por ejemplo:
```sh
$ mosquitto_pub -t "actuadores/luces/1" -m 1
```

Verificar de esta manera el correcto funcionamiento de cada actuador disponible. 

### 3 - Script controlador de actuadores
Tome el script "controlador.py" el cual viene con una interfaz de usuario por consola que le permitira accionar sobre los distintos actuadores. Deberá agregar a este script lo necesario para que el controlador se conecte por MQTT.

Agregar al script las librerías que necesitaremos de MQTT:
```python
import paho.mqtt.client as paho
```

Utilice las variables de entorno definidas en el archivo ".env" almacenadas dentro de la variable "config"
```python
broker = config["BROKER"]
port = int(config["PORT"])
```

Crear la función de "on_connect" que utilizaremos para verificar que nuestro script pude conectarse exitosamente a la aplicación:
```python
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt conectado")
    else:
        print(f"Mqtt connection faild, error code={rc}")
```

Crear el cliente MQTT y conectarse la IP y puerto definidos:
```python
client = paho.Client("controlador")
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()
```

Agregar a la función "controlador" la lógica necesaria para forma el tópico y publicar el mensaje por MQTT.
```python
def controlador(actuador, valor):
    # Agregar lógica necesaria
    pass
```

Finalizar el script con la desconexión del publicador y la finalización del cliente MQTT:
```python
client.disconnect()
client.loop_stop()
```
