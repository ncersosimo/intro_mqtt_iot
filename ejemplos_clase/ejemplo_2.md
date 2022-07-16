# Ejemplos de clase

En esta práctica el objetivo es repetir la experiencia de enviar y recibir mensajes MQTT pero esta vez con la aplicación de MQTTExplorer.

Estructura de tópicos a utilizar:
|           |            |             |        |
| ----------| --------   | ------------| ------ |
|  sensores | cocina     | temperatura | 1, 2, 3 ....
|  sensores | cocina     | humedad     | 1, 2, 3 ....
|  sensores | salon      | temperatura | 1, 2, 3 ....
|  sensores | salon      | humedad     | 1, 2, 3 ....
|  sensores | dormitorio | temperatura | 1, 2, 3 ....
|  sensores | dormitorio | humedad     | 1, 2, 3 ....

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

### 1 - Comodín #
Abrir MQTTExplorer. Conectar la app al broker indicando la IP del dispositivo.

Desde la terminal suscribrse utilizando el comodín "#" para recibir cualquier número de sensor, por ejemplo:
```sh
$ mosquitto_sub -v -t sensores/cocina/temperatura/#
```

Desde MQTTExplorer publicar datos raw y JSONString a distintos tópicos de temperatura, y a distintas locaciones (cocina, salon, etc) y observar que mensajes llegan y que mensajes no.

### 2 - Comodín +
Desde la terminal suscribrse utilizando el comodín "+" para recibir datos del sensor de temperatura 1 de cualquier locación:
```sh
$ mosquitto_sub -v -t sensores/+/temperatura/1
```

Desde MQTTExplorer publicar datos raw y JSONString a distintos tópicos de temperatura, y a distintas locaciones (cocina, salon, etc) y observar que mensajes llegan y que mensajes no.

### 3 - Comodín # y +
Desde la terminal suscribrse utilizando el comodín "#" para recibir cualquier número de sensor, utilizarel comodín "+" para recibir datos de cualquier locación, por ejemplo:
```sh
$ mosquitto_sub -v -t sensores/+/temperatura/#
```

Desde MQTTExplorer publicar datos raw y JSONString a distintos tópicos de temperatura, y a distintas locaciones (cocina, salon, etc) y observar que mensajes llegan y que mensajes no.


Desde la terminal suscribrse utilizando el comodín "#" para recibir datos de cualquier sensor o locación, por ejemplo:
```sh
$ mosquitto_sub -v -t sensores/#
```

Desde MQTTExplorer publicar datos raw y JSONString a distintos tópicos de temperatura, y a distintas locaciones (cocina, salon, etc) y observar que mensajes llegan y que mensajes no.