

#FUNCIONALIDAD 1: mostrar listado de artistas
def mostrarListadoConciertos():
    '''
    Muestra el listado de los conciertos disponibles de cada artista
    Return: no retorna nada, solo imprime
    '''
    artistas = [
        # nombre artista - género
        ["Olivia Rodrigo", "Pop"],
        ["Arctic Monkeys", "Rock Alternativo"],
        ["The Strokes", "Rock Alternativo"],
        ["Twenty One Pilots", "Rock Alternativo"],
        ["Linkin Park", "Rock"],
        ["Bring Me The Horizon", "Rock Alternativo"],
        ["Kriett", "Heavy Metal"]
    ]
    
    print("-" * 70)
    print("\nElegí tu concierto:\n")
    for artista in artistas:
        nombre, genero = artista
        print("- %s" %nombre)
    print("-" * 70)


def elegirBanda():
    '''
    Que hace
    Que parametros tiene
    que retorna 
    '''
    pass 

def main():
    mostrarListadoConciertos()

main() 
