# SISTEMA DE GESTION DE CONCIERTOS EN UN ESTADIO


#FUNCIONALIDAD 1: mostrar listado de artistas
def mostrarListadoArtistas():
    '''
    Que hace
    Que parametros tiene
    que retorna 
    '''
    pass 

def elegirBanda():
    '''
    Que hace
    Que parametros tiene
    que retorna 
    '''
    pass 

# FUNCIONALIDAD 2 - elegir fecha
def elegirFecha(artista):
    '''
    Que hace -> La función maneja el proceso de seleccion de fecha
    Que parametros tiene -> artista 
    que retorna -> fecha elegida
    '''
    artistas = [artista1, artista2, artista3]
    fecha_por_artista = [
        ["11/05/2025", "12/05/2025", "13/05/2025"]
        ["03/06/2025", "04/06/2025"]
        ["20/07/2025"]
    ]
    for i in range (len(artistas)):
        if artistas[i] == artista:
            fechas_disponibles = fecha_por_artista[i]
            break
    
    for i, fecha in enumerate(fechas_disponibles, start = 1):
        print(f"{i}. {fecha}")
    seleccionar_fecha = int(input("Por favor, ingrese el numero de fecha escogido"))
    while seleccionar_fecha < 1 or seleccionar_fecha > len(fechas_disponibles):
        print("Fecha invalida, intente nuevamente")

    fecha_elegida = fechas_disponibles[seleccionar_fecha - 1]
    return fecha_elegida
# FUNCIONALIDAD 3 - elegir asientos

def elegirUbicacion():
    '''
    Que hace
    Que parametros tiene
    que retorna 
    '''
    pass 

def elegirAsientosEnUbicacion():
    '''
    Que hace
    Que parametros tiene
    que retorna 
    '''
    pass 

# FUNCIONALIDAD 4 - ingresar datos

def agregarDatosDeReserva():
    '''
    Que hace
    Que parametros tiene
    que retorna 
    '''
    pass 

def buscarReserva():
    '''
    Que hace
    Que parametros tiene
    que retorna 
    '''
    pass 

def elegirMedioDePago():
    '''
    Que hace
    Que parametros tiene
    que retorna 
    '''
    pass 

# FUNCIONALIDAD 5 - 
def pagarEntrada():
    '''
    Que hace
    Que parametros tiene
    que retorna 
    '''
    pass 

def cargarEntradaDeCliente(cliente):
    '''
    Que hace
    Que parametros tiene
    que retorna 
    '''
    pass 

# FUNCIONALIDAD 6 - confirmar e imprimir boleta y entrada
def imprimirBoleta():
    '''
    Que hace
    numero de transaccion random
    Que parametros tiene
    que retorna 
    '''
    pass 

def imprimirEntrada():
    '''
    Que hace
    Que parametros tiene
    que retorna 
    '''
    pass 


# Programa principal

def main():
    '''
    Que hace (menu de usuario)
    Que parametros tiene
    que retorna 
    '''
    pass 






