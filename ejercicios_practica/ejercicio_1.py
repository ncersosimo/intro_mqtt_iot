import json
import paho.mqtt.client as paho
from dotenv import dotenv_values

config = dotenv_values()
joystick = {}
opciones = ["FIN", "Luces", "Volar", "Motores", "Joystick"]

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt conectado")
    else:
        print(f"Mqtt no conectado, codigo error={rc}")


def controlador(client, topico, valor):
    client.publish(topico, valor)

def devolver_opciones():
    # Recorre los valores de la lista opciones
    # para generar las mismas automáticamente
    # en el menú
    cadena = ''.join([f'\n\t {indice + 1} - {opcion}' for indice, opcion in enumerate(opciones)]) + "\n"
    return cadena 

if __name__ == "__main__":

    client = paho.Client("controlador")
    client.on_connect = on_connect
    client.connect(config["BROKER"], int(config["PORT"]))
    client.loop_start()

    while True:        
        opcion = int(input("Ingrese la opcion del actuador que desea controlar " 
        ", o seleccione FIN para salir: " + devolver_opciones()))
        
        print(f"Opción seleccionada: {opcion} - {opciones[opcion - 1]}")
        actuador = opciones[opcion - 1].lower()
        topico = f"actuadores/{actuador}"

        if actuador == "fin":
            print("Fin de la ejecucion")
            break
        elif actuador == "luces":
            topico += "/1"
        elif actuador == "motores":
            valor = int(input("Ingrese el motor que desea controlar (1..4): "))
            topico += f"/{valor}"     
          
        if actuador == "joystick":
            valor = float(input("Ingrese el valor que desea enviar para X (-1 a 1): "))
            joystick["x"] = valor
            valor = float(input("Ingrese el valor que desea enviar para Y (0 a 1): "))
            joystick["y"] = valor
            # Convierto el diccionario a un JSON String            
            valor = json.dumps(joystick)
            print(f"Topico: {topico}")
            print(f"Valor: {valor}")    
        else:
            valor = int(input("Ingrese el valor que desea enviar: "))    
        
        controlador(client, topico, valor)

    client.disconnect()
    client.loop_stop()


#     Topicos que soporta este mock drone emulado:
# |             |          |      | datos ejemplo
# | ----------  | -------- | -----| -----
# |  actuadores | luces    | 1    |  0/1
# |  actuadores | volar    |      |  0/1
# |  actuadores | motores  | 1..4 |  0/1
# |  actuadores | joystick |      |  {"x": 0.8, "y": 0.3}

# Joystick:
# - Tener en cuenta que este tópico recibe un JSON String. Debe armar el payload como un JSON/diccionario y pasarlo a JSON String con json.dumps
# - El joytsick soporta para valores de "x" de -1 a 1.
# - El joytsick soporta para valores de "y" de 0 a 1.