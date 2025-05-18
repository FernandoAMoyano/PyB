"""
Este módulo contiene las funciones para gestionar los dispositivos
"""

from data.data import listado_dispositivos


def mostrar_dispositivos(listado):
    print("\n" + "-" * 30)
    print("📃 LISTADO DE DISPOSITIVOS:")
    print("-" * 30)
    if not listado:
        print("⚠️ No hay dispositivos registrados.")
    else:
        for i, dispositivo in enumerate(listado):
            print(f"💡{i+1}){dispositivo['nombre']}")


def agregar_dispositivo(nuevo_dispositivo):

    dispositivo = {
        "categoria": nuevo_dispositivo["categoria"],
        "alimentacion": nuevo_dispositivo["alimentacion"],
        "consumo": nuevo_dispositivo["consumo"],
        "ubicacion": nuevo_dispositivo["ubicacion"],
        "estado": False,
        "marca": nuevo_dispositivo["marca"],
        "nombre": nuevo_dispositivo["nombre"],
    }

    listado_dispositivos.append(dispositivo)
    print("\n" + "-" * 50)
    print(f"✅ Dispositivo {nuevo_dispositivo['nombre']} agregado con exito!!")
    print("-" * 50)


def buscar_dispositivo(lista, nombre):
    dispositivo_encontrado = False
    
    for dispositivo in lista:
        if dispositivo["nombre"] == nombre:
            print("\n" + "-" * 50)
            print(f"✔️ El Dispositivo {nombre} está dentro de tu lista")
            print("-" * 50)
            dispositivo_encontrado = True
            break
    if not dispositivo_encontrado:
        print(f"\n ❌ No se encontro el dispositivo {nombre}\n Recueda escribir correctamente el nombre!!")


def eliminar_dispositivo(dispositivo_a_eliminar):
    dispositivo_encontrado = False
    for dispositivo in listado_dispositivos:
        if dispositivo["nombre"] == dispositivo_a_eliminar:
            listado_dispositivos.remove(dispositivo)
            print("\n" + "-" * 50)
            print(f"✅ Eliminacion exitosa, {dispositivo_a_eliminar} fue removido")
            print("-" * 50)
            dispositivo_encontrado = True
            break

    if not dispositivo_encontrado:
        print("\n" + "-" * 50)
        print(f'❌ No se encontró el dispositivo "{dispositivo_a_eliminar}"\n recuerda escribir correctamente el nombre!!')
        print("-" * 50)


def cambiar_estado_dispositivo(lista, nombre):
    dispositivo_encontrado = False

    for dispositivo in lista:
        if dispositivo["nombre"] == nombre:
            estado = "encendido" if dispositivo["estado"] == False else "apagado"
            dispositivo["estado"] = estado
            dispositivo_encontrado = True
            print("\n" + "-" * 50)
            print(f"  🕹️ El dispositivo ahora se encuentra {estado}")
            print("-" * 50)
            break
    if not dispositivo_encontrado:
        print("No se encontró el dispositivo")
