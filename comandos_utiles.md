# Comandos básicos de consola de linux

Lanzar el mosquitto MQTT broker
```sh
$ mosquitto
```

Verificar que el servicio este en ejecución, en este caso el servicio de mosquitto:
```sh
$ sudo systemctl status <nombre_servicio>
```

Verificar que aplicaciones está utilizando cada puerto del sistema:
```sh
$ sudo netstat -tulpn
```

Suscribirse a un tópico MQTT con mosquitto_sub:
```sh
$ mosquitto_sub -t <nombre_topico>
```

Publicar a un tópico MQTT con mosquitto_pub:
```sh
$ mosquitto_pub -t <nombre_topico> -m <mensaje>
```