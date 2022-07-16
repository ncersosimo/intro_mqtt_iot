import paho.mqtt.client as paho

broker = "localhost"
port = 1883

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt conectado")
    else:
        print(f"Mqtt connection faild, error code={rc}")


def controlador(actuador, numero, valor):
    pass


if __name__ == "__main__":

    client = paho.Client("controlador")
    client.on_connect = on_connect
    client.connect(broker, port)
    client.loop_start()

    print("Drone Mock: Sistema controlador de actuadores")

    while True:
        actuador = input("Ingrese que actuador desea controlar, o escriba FIN para salir: ").lower()
        if actuador == "fin":
            break

        numero = 0
        if actuador != "vuelo":
            numero = int(input("Ingrese el numero de actuador a manipular: "))

        valor = int(input("Ingrese el valor que desea enviar: "))
        controlador(actuador, numero, valor)


    client.disconnect()
    client.loop_stop()