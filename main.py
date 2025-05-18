"""
Archivo principal del sistema SmartHome
"""

import dispositivos
from data.data import listado_dispositivos
from utilities import inputs
import modo_sleep


print("\n" + "-" * 30)
print("⚡Bienvenido a Smart Home⚡")
print("-" * 30)


while True:
   opciones_menu = inputs.mostrar_menu()
   match opciones_menu:
        case 1:
            dispositivos.mostrar_dispositivos(listado_dispositivos)     
        case 2:
            nuevo_dispositivo = inputs.pedir_datos()
            dispositivos.agregar_dispositivo(nuevo_dispositivo)
        case 3:
            dispositivo_a_buscar=input("Ingresa el nombre del dispositivo que quieres buscar :")
            dispositivos.buscar_dispositivo(listado_dispositivos, dispositivo_a_buscar)
        case 4:
           dispositivo_a_eliminar=input("Ingresa el nombre del dispositivo a eliminar : ")
           dispositivos.eliminar_dispositivo(dispositivo_a_eliminar) 
        case 5:
          modo_sleep.ejecutar_modo_sueño()
          print("Automatizando....")
        case 6:
          dispositivo_a_modificar =input("Ingresa el nombre del dispositivo al que quieres cambiarle el estado : ")
          dispositivos.cambiar_estado_dispositivo(listado_dispositivos, dispositivo_a_modificar)
        case 7:
            print("\n👋🏾 Hasta luego!! vuelve pronto, te estaremos esperando 😀")
            break
