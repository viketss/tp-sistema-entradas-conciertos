def elegir_platea():
    """
    Función para gestionar la selección del tipo de platea/asiento.
    """
    # Definir los tipos de asientos disponibles como una lista
    opciones_validas = ["CD", "Preferencial", "Platea Baja", "Platea Alta", "Campo Trasero", "Campo Delantero"]
    
    # Mostrar opciones de asientos
    print("\n=== SELECCIÓN DE TIPO DE ASIENTO ===")
    print("Tipos de asientos disponibles:")
    for i in range(len(opciones_validas)):
        print(f"{i+1}. {opciones_validas[i]}")
    
    # Seleccionar tipo de asiento
    tipo_asiento = None
    while tipo_asiento is None:
        seleccion = input("\nSeleccione el tipo de asiento (número): ")
        # Validar que sea un número
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
    # Seleccionar cantidad de asientos
    cantidad_asientos = 0
    while cantidad_asientos <= 0:
        cantidad_input = input("\nIngrese la cantidad de asientos deseada: ")
        # Validar que sea un número
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
    precio_base = 5000  # $5000 como se muestra en el diagrama
    
    # Lista de tipos de asientos y factores (como matriz)
    # [tipo_asiento, factor]
    factores_lista = [
        ["CD", 1.5],
        ["Preferencial", 1.3],
        ["Platea Bajas", 1.0],
        ["Platea Altas", 0.8],
        ["Campo Trasero", 1.2],
        ["Campo Delantero", 2.0]
    ]
    
    # Buscar el factor correspondiente al tipo de asiento
    factor = 1.0  # Valor por defecto
    for asiento in factores_lista:
        if asiento[0] == tipo_asiento:
            factor = asiento[1]
    
    precio_total = precio_base * factor * cantidad_asientos
    
    # Mostrar resumen de la selección
    print("\n=== RESUMEN DE SELECCIÓN ===")
    print(f"Tipo de asiento: {tipo_asiento}")
    print(f"Cantidad: {cantidad_asientos}")
    print(f"Precio base: ${precio_base}")
    print(f"Factor de precio: {factor}")
    print(f"Precio total: ${precio_total:.2f}")
    
    return precio_total


def confirmar_seleccion(tipo_asiento, cantidad_asientos, precio_total):
    """
    Función para confirmar la selección realizada.
    """
    confirmacion = None
    while confirmacion not in ["s", "n"]:
        confirmacion = input("\n¿Confirma su selección? (s/n): ").lower()
        if confirmacion == "s":
            print("Selección confirmada.")
            # Devolver una lista con la información
            return [tipo_asiento, cantidad_asientos, precio_total]
        elif confirmacion == "n":
            print("Selección cancelada. Vuelva a intentarlo.")
            return None
        else:
            print("Opción no válida. Ingrese 's' para confirmar o 'n' para cancelar.")


def proceso_seleccion_completo():
    """
    Función que coordina todo el proceso de selección.
    """
    seleccion_completada = False
    resultado = None
    
    while not seleccion_completada:
        # Paso 1: Elegir platea/tipo de asiento
        tipo_asiento = elegir_platea()
        
        # Paso 2: Elegir cantidad de asientos
        cantidad_asientos = elegir_cantidad_asientos()
        
        # Calcular precio
        precio_total = calcular_precio(tipo_asiento, cantidad_asientos)
        
        # Confirmar selección
        resultado = confirmar_seleccion(tipo_asiento, cantidad_asientos, precio_total)
        
        if resultado is not None:
            seleccion_completada = True
    
    return resultado


if __name__ == "__main__":
    seleccion = proceso_seleccion_completo()
    if seleccion:
        print(f"Tipo de asiento seleccionado: {seleccion[0]}")
        print(f"Cantidad de asientos: {seleccion[1]}")
        print(f"Precio total: ${seleccion[2]:.2f}")