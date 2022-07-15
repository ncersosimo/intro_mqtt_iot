# Ejemplos de clase

Mencionar que en la raiz del repo encontrará un archivo de "comandos_utiles" con los comandos básicos de linux que utilizaremos esta clase.

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

Conectarse por ssh desde una terminal del host
```
$ ssh inove@<ip_dispositivo>
```

Verificar que el MQTT broker está lanzado:
```sh
$ sudo systemctl status mosquitto
```

Verificar que el MQTT broker está tomando el puerto 1883:
```sh
$ sudo netstat -tulpn
```

Si mosquitto MQTT broker no está lanzado, ejecutar:
```sh
$ mosquitto
```

Si mosquitto MQTT no está instalado ejecutar:
```sh
$ sudo apt-get install -y mosquitto mosquitto-clients
```

Suscriberse al tópico "sensores/temperatura/1" desde la consola. La consola quedará tomada a la espera de los mensajes provenientes de este tópico:
```sh
$ mosquitto_sub -t sensores/temperatura/1 
```

Logearse desde otra terminal por ssh. Enviar un mensaje al tópico sensores/temperatura/1  en formato "raw". Al enviar el mensaje deberemos ver en la otra terminal como llega el dato enviado:
```sh
$ mosquitto_pub -t sensores/temperatura/1 -m 24
```

Repetir la experiencia, pero ahora enviado un mensaje en formato JSON:
```sh
$ mosquitto_pub -t sensores/temperatura/1 -m "{temp: 24}"
```

Cerrar el proceso de la terminal con mosquitto_sub. Volver a suscribirse pero ahora utilizando el comodin "#" para recibir datos de cualquier número de sensor:
```sh
$ mosquitto_sub -t sensores/temperatura/#
```

Desde la segunda terminal realizar diferentes publicaciones como si fueran distintos números de sensores y demostrar como funciona el "#", por ejemplo:
```sh
$ mosquitto_pub -t sensores/temperatura/3 -m "{temp: 24}"
```
