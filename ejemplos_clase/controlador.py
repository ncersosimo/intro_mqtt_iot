from dotenv import dotenv_values

config = dotenv_values()

def controlador(client, actuador, valor):
    pass


if __name__ == "__main__":

    # Aquí conectarse a MQTT

    print("Drone Mock: Sistema controlador de actuadores")

    while True:
        actuador = input("Ingrese que actuador desea controlar, o escriba FIN para salir: ").lower()
        if actuador == "fin":
            break

        valor = int(input("Ingrese el valor que desea enviar: "))
        controlador(client, actuador, valor)
