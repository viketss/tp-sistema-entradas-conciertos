def elegir_banda():
    """
    Función para gestionar la selección de la banda.
    """
    bandas = ["Tan Bionica", "Linkin Park", "Olivia Rodrigo"]
    print("\n=== SELECCIÓN DE BANDA ===")
    for i, banda in enumerate(bandas, start=1):
        print(f"{i}. {banda}")
    
    seleccion = None
    while seleccion is None:
        seleccion = input("\nSeleccione la banda (número): ")
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(bandas):
                banda_elegida = bandas[seleccion - 1]
                print(f"Ha seleccionado: {banda_elegida}")
                return banda_elegida
            else:
                print("Opción no válida. Intente nuevamente.")
                seleccion = None
        else:
            print("Por favor, ingrese un número válido.")
            seleccion = None


def elegir_fecha(artista):
    """
    Función para gestionar la selección de la fecha según la banda.
    """
    artistas = ["Tan Bionica", "Linkin Park", "Olivia Rodrigo"]
    fecha_por_artista = [
        ["10/05/2025", "11/05/2025", "12/05/2025"],
        ["03/06/2025", "04/06/2025"],
        ["20/07/2025"]
    ]
    
    fechas_disponibles = None
    for i in range(len(artistas)):
        if artistas[i] == artista:
            fechas_disponibles = fecha_por_artista[i]
            break
    
    if fechas_disponibles is None:
        print("Artista no encontrado.")
        return None

    print("\n=== SELECCIÓN DE FECHA ===")
    for i, fecha in enumerate(fechas_disponibles, start=1):
        print(f"{i}. {fecha}")
    
    seleccionar_fecha = None
    while seleccionar_fecha is None:
        seleccionar_fecha = input("Por favor, ingrese el número de fecha escogido: ")
        if seleccionar_fecha.isdigit():
            seleccionar_fecha = int(seleccionar_fecha)
            if 1 <= seleccionar_fecha <= len(fechas_disponibles):
                fecha_elegida = fechas_disponibles[seleccionar_fecha - 1]
                print(f"Fecha seleccionada: {fecha_elegida}")
                return fecha_elegida
            else:
                print("Fecha inválida, intente nuevamente.")
                seleccionar_fecha = None
        else:
            print("Por favor, ingrese un número válido.")
            seleccionar_fecha = None


def elegir_platea():
    """
    Función para gestionar la selección del tipo de platea/asiento.
    """
    opciones_validas = ["CD", "Preferencial", "Platea Baja", "Platea Alta", "Campo Trasero", "Campo Delantero"]
    
    print("\n=== SELECCIÓN DE TIPO DE ASIENTO ===")
    for i, opcion in enumerate(opciones_validas, start=1):
        print(f"{i}. {opcion}")
    
    tipo_asiento = None
    while tipo_asiento is None:
        seleccion = input("\nSeleccione el tipo de asiento (número): ")
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(opciones_validas):
                tipo_asiento = opciones_validas[seleccion - 1]
                print(f"Ha seleccionado: {tipo_asiento}")
            else:
                print("Opción no válida. Intente nuevamente.")
        else:
            print("Por favor, ingrese un número válido.")
    
    return tipo_asiento


def elegir_cantidad_asientos():
    """
    Función para gestionar la selección de la cantidad de asientos.
    """
    cantidad_asientos = 0
    while cantidad_asientos <= 0:
        cantidad_input = input("\nIngrese la cantidad de asientos deseada: ")
        if cantidad_input.isdigit():
            cantidad_asientos = int(cantidad_input)
            if cantidad_asientos > 0:
                print(f"Cantidad seleccionada: {cantidad_asientos} asiento(s)")
            else:
                print("La cantidad debe ser un número positivo.")
        else:
            print("Por favor, ingrese un número válido.")
    
    return cantidad_asientos


def calcular_precio(tipo_asiento, cantidad_asientos):
    """
    Función para calcular el precio total según el tipo y cantidad de asientos.
    """
    precio_base = 5000
    factores_lista = [
        ["CD", 1.5],
        ["Preferencial", 1.3],
        ["Platea Baja", 1.0],
        ["Platea Alta", 0.8],
        ["Campo Trasero", 1.2],
        ["Campo Delantero", 2.0]
    ]
    
    factor = 1.0
    for asiento in factores_lista:
        if asiento[0] == tipo_asiento:
            factor = asiento[1]
    
    precio_total = precio_base * factor * cantidad_asientos
    
    print("\n=== RESUMEN DE SELECCIÓN ===")
    print(f"Tipo de asiento: {tipo_asiento}")
    print(f"Cantidad: {cantidad_asientos}")
    print(f"Precio base: ${precio_base}")
    print(f"Factor de precio: {factor}")
    print(f"Precio total: ${precio_total:.2f}")
    
    return precio_total


def confirmar_pago():
    """
    Función para confirmar el pago.
    """
    confirmacion = None
    while confirmacion not in ["s", "n"]:
        confirmacion = input("\n¿Desea confirmar el pago? (s/n): ").lower()
        if confirmacion == "s":
            print("Pago confirmado. Imprimiendo boleta...")
            return True
        elif confirmacion == "n":
            print("Pago cancelado.")
            return False
        else:
            print("Opción no válida. Intente nuevamente.")


def main():
    """
    Función principal que coordina todo el flujo del programa.
    """
    print("=== SISTEMA DE ENTRADAS PARA ESPECTÁCULOS ===")
    
    # Paso 1: Elegir banda
    banda = elegir_banda()
    
    # Paso 2: Elegir fecha
    fecha = elegir_fecha(banda)
    
    # Paso 3: Elegir tipo de asiento
    tipo_asiento = elegir_platea()
    
    # Paso 4: Elegir cantidad de asientos
    cantidad_asientos = elegir_cantidad_asientos()
    
    # Paso 5: Calcular precio
    precio_total = calcular_precio(tipo_asiento, cantidad_asientos)
    
    # Paso 6: Confirmar pago
    if confirmar_pago():
        print("\n=== RESUMEN DE COMPRA ===")
        print(f"Banda: {banda}")
        print(f"Fecha: {fecha}")
        print(f"Tipo de asiento: {tipo_asiento}")
        print(f"Cantidad de asientos: {cantidad_asientos}")
        print(f"Precio total: ${precio_total:.2f}")
        print("¡Gracias por su compra!")
    else:
        print("La compra ha sido cancelada.")


if __name__ == "__main__":
    main()