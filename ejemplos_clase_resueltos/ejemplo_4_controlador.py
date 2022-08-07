import paho.mqtt.client as paho
from dotenv import dotenv_values

config = dotenv_values()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt conectado")
    else:
        print(f"Mqtt connection faild, error code={rc}")


def controlador(client, actuador, valor):
    topico = f"actuadores/{actuador}"
    if actuador == "luces":
        topico += "/1"
    client.publish(topico, valor)


if __name__ == "__main__":

    client = paho.Client("controlador")
    client.on_connect = on_connect
    client.connect(config["BROKER"], int(config["PORT"]))
    client.loop_start()

    print("Drone Mock: Sistema controlador de actuadores")

    while True:
        actuador = input("Ingrese que actuador desea controlar, o escriba FIN para salir: ").lower()
        if actuador == "fin":
            break

        valor = int(input("Ingrese el valor que desea enviar: "))
        controlador(client, actuador, valor)

    client.disconnect()
    client.loop_stop()