
def pedir_datos():
    return {
        "categoria": input("Ingresa La cateoria del dispositivo :"),
        "alimentacion": input("Ingresa el tipo de alimentacion del dispositivo :"),
        "consumo": input("Ingresa el tipo de consumo del dispositivo :"),
        "ubicacion": input("Ingresa la ubicacion del dispositivo : "),
        "marca": input("Ingresa La marca del dispositivo : "),
        "nombre": input("Ingresa el nombre del dispostivo :"),
    }

def mostrar_menu():
     seleccion_usuario = int(
        input(
            "\nA continuacion ingresa la operación que quieres ejecutar\n\n 1. Mostrar dispositivos\n 2. Agregar dispositivo\n 3. Buscar dispositivo \n 4. Eliminar dispositivo\n 5️. iniciar modo sueño \n 6. Cambiar estado del dispositivo\n 7. Salir\n"
        )
    )
     return seleccion_usuario
 
