"""
Este módulo implementa la funcionalidad del modo sueño para los dispositivos
"""

from data.data import DISPOSITIVOS_ORIGINALES, listado_dispositivos

def ejecutar_modo_sueño():
    print("\n" + "-" * 40)
    print("💤 MODO SUEÑO 💤")
    print("-" * 40)
    
    # Mostrar dispositivos originales disponibles
    print("\nDispositivos disponibles:")
    for i, nombre in enumerate(DISPOSITIVOS_ORIGINALES, 1):
        print(f"{i}) {nombre}")
    
    # Seleccionar dispositivo
    seleccion = input("\nSelecciona un dispositivo (número): ")
    
    try:
        indice = int(seleccion) - 1
        if 0 <= indice < len(DISPOSITIVOS_ORIGINALES):
            dispositivo_seleccionado = DISPOSITIVOS_ORIGINALES[indice]
            
            # Aplicar configuración específica según el dispositivo
            if dispositivo_seleccionado == "Televisor":
                print("\n" + "-" * 50)
                print(f"\n✅ {dispositivo_seleccionado} con brillo reducido")
                print("📺 Brillo ajustado al 30%")
                print("-" * 50)
                
            elif dispositivo_seleccionado == "barra de sonido":
                print("\n" + "-" * 50)
                print(f"\n✅ {dispositivo_seleccionado} con volumen reducido")
                print("🔊 Volumen ajustado al 20%")
                print("-" * 50)
                
            elif dispositivo_seleccionado == "Aire acondicionado":
                print("\n" + "-" * 50)
                print(f"\n✅ {dispositivo_seleccionado} configurado en modo ECO")
                print("❄️ Temperatura ajustada a 24°C")
                print("-" * 50)
            
            print("🔋 Dispositivo en modo de bajo consumo")
            print("-" * 50)
        else:
            print("\n❌ Selección inválida")
    except ValueError:
        print("\n❌ Por favor, ingresa un número válido")