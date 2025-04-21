"""
Hola Chona, somos Timo C, Mayte C y Juli W. En este proyecto nos ayudamos mucho de Copilot, pero fuimos cambiando el código o partes que
no enseñaste (tales como if not in, etc), la verdad nos ayudo mucho utilizar esta herramienta para entender la sintaxis, y no
creo que nos afecte usar mucho una IA en proyecto. Sabemos que al final tenemos que comprender que hay escrito en el mismo y 
como funciona.

Continue fue algo que aprendimos en este proyecto buscando en stackoverflow y nos pareció mejor que usar return
ya que sino habría que empezar todo devuelta.

https://www.w3schools.com/python/ref_keyword_continue.asp
https://docs.python.org/es/3.13/library/random.html
https://www.w3schools.com/python/ref_keyword_break.asp
https://chatgpt.com/share/68046873-992c-800c-910c-d289c1442b81 - a modo de inspiracion para ordenar las ideas
https://codefinity.com/blog/All-About-Exceptions-in-Python-and-How-to-Catch-Them?utm_source=google&utm_medium=cpc&utm_campaign=21380043065&utm_content=&utm_term=&dki=&gad_source=1&gclid=CjwKCAjwk43ABhBIEiwAvvMEB_NS96ZLWARDMlLEJ_-lEDzMkYnOfQJTPuZz2UvW21nOOlC_r9bjDBoCHswQAvD_BwE

"""

# Llamado a la libreria de python
import random

# Funcion para crear un tablero vacio de tamaño N x N, usando list list bool
def crear_tablero(tamano):

    #Crea un tablero de tamaño N x N - inicia con False (sin barcos)

    return [[False for _ in range(tamano)] for _ in range(tamano)]

# Funcion para imprimir el tablero
def imprimir_tablero(tablero, revelar_barcos = False):

   #Imprime el tablero. Si revelar_barcos es True, muestra la ubicacion de los barcos

    for fila in tablero:
        print(" ".join("❌" if celda is True and revelar_barcos else "❌" if celda == "❌" else "🧊" if celda == "🧊" else "❔" for celda in fila))

    #Funcion que le permite a un jugador poner manualmente los barcos en el tablero
def colocar_barcos_manual(tablero, cantidad_barcos):

    print("\nColoca tus barcos en el tablero.")
    for i in range(cantidad_barcos):
        while True:
        # Detecta errores - Si se llegan a equivocar el código no falla y te muestra un mensaje de error
            try:
                print(f"\nColocando barco {i + 1} (puede ocupar hasta 3 casillas).")
                fila = int(input(f"Ingrese la fila inicial (0-{len(tablero) - 1}): "))
                columna = int(input(f"Ingrese la columna inicial (0-{len(tablero) - 1}): "))
                orientacion = input("Ingrese la orientación (H para horizontal, V para vertical): ")
                tamano_barco = int(input("Ingrese el tamaño del barco (1-3): "))
                
                # Valida el tamaño del barco
                if tamano_barco < 1 or tamano_barco > 3:
                    print("El tamaño del barco debe estar entre 1 y 3.")
                    continue 
                    # Si esto no se cumple, vuelve al while true para no salir del bucle
                
                # Valida la orientacion
                if orientacion != "H" and orientacion != "V":
                    print("Orientación inválida. Use 'H' para horizontal o 'V' para vertical.")
                    continue

                # Verifica si el barco entra en el tablero
                if orientacion == "H" and columna + tamano_barco > len(tablero):
                    print("El barco no entra horizontalmente en esta posición.")
                    continue
                if orientacion == "V" and fila + tamano_barco > len(tablero):
                    print("El barco no entra verticalmente en esta posición.")
                    continue

                # Verifica si las posiciones estan desocupadas
                posiciones_validas = True
                for j in range(tamano_barco):
                    if orientacion == "H" and tablero[fila][columna + j]:
                        posiciones_validas = False
                        # Rompe el ciclo de un while for, no como continue que te manda al siguiente
                        break
                    if orientacion == "V" and tablero[fila + j][columna]:
                        posiciones_validas = False
                        break

                if not posiciones_validas:
                    print("Una o mas posiciones ya están ocupadas. Intenta de nuevo.")
                    continue

                # Coloca el barco en el tablero
                for j in range(tamano_barco):
                    if orientacion == "H":
                        tablero[fila][columna + j] = True
                    else:
                        tablero[fila + j][columna] = True

                break
            except ValueError:
                print("Por favor, ingrese valores validos.")

# Funcion principal del juego
def jugar():
    print("¡Bienvenido a Batalla Naval!")

    # Pide el tamaño del tablero
    while True:
        try:
            tamano_tablero = int(input("Ingrese el tamaño del tablero (ej: 10 para un tablero 10x10): "))
            if tamano_tablero <= 0:
                print("El tamaño del tablero debe ser un numero positivo mayor a 0")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un numero válido.")

    # Pide la cantidad de barcos
    while True:
        try:
            cantidad_barcos = int(input(f"Ingrese la cantidad de barcos (máximo {tamano_tablero * tamano_tablero}): "))
            if cantidad_barcos <= 0 or cantidad_barcos > tamano_tablero * tamano_tablero:
                print(f"La cantidad de barcos debe estar entre 1 y {tamano_tablero * tamano_tablero}.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un numero válido.")

    # Crea tableros para ambos jugadores
    tablero_jugador1 = crear_tablero(tamano_tablero)
    tablero_jugador2 = crear_tablero(tamano_tablero)

    # Coloca barcos manualmente para ambos jugadores
    print("\nJugador 1, coloque sus barcos:")
    colocar_barcos_manual(tablero_jugador1, cantidad_barcos)
    print("\nJugador 2, coloque sus barcos:")
    colocar_barcos_manual(tablero_jugador2, cantidad_barcos)

    # Tableros visibles
    tablero_visible_jugador1 = [["❔" for _ in range(tamano_tablero)] for _ in range(tamano_tablero)]
    tablero_visible_jugador2 = [["❔" for _ in range(tamano_tablero)] for _ in range(tamano_tablero)]

    # Turnos de los jugadores
    disparos_restantes = cantidad_barcos * 2
    disparos_acertados_jugador1 = 0
    disparos_acertados_jugador2 = 0

    turno_jugador = 1
    while disparos_restantes > 0:
        print(f"\nTurno del Jugador {turno_jugador}")
        if turno_jugador == 1:
            imprimir_tablero(tablero_visible_jugador2)
        else:
            imprimir_tablero(tablero_visible_jugador1)

        try:
            fila = int(input(f"Ingrese la fila (0-{tamano_tablero-1}): "))
            columna = int(input(f"Ingrese la columna (0-{tamano_tablero-1}): "))
        except ValueError:
            print("Por favor, ingrese numeros válidos.")
            continue

        # Valida las coordenadas
        if fila < 0 or fila >= tamano_tablero or columna < 0 or columna >= tamano_tablero:
            print("Coordenadas fuera de rango, intente de nuevo.")
            continue

        # Verifica el disparo
        if turno_jugador == 1:
            tablero_oponente = tablero_jugador2
            tablero_visible = tablero_visible_jugador2
            disparos_acertados = disparos_acertados_jugador1
        else:
            tablero_oponente = tablero_jugador1
            tablero_visible = tablero_visible_jugador1
            disparos_acertados = disparos_acertados_jugador2

        if tablero_oponente[fila][columna] is True:
            print("¡Acertaste! Le diste a un barco.")
            tablero_oponente[fila][columna] = "❌"
            tablero_visible[fila][columna] = "❌"
            if turno_jugador == 1:
                disparos_acertados_jugador1 += 1
            else:
                disparos_acertados_jugador2 += 1
        elif tablero_oponente[fila][columna] in ["❌", "🧊"]:
            print("Ya disparaste a ese barco, intenta de nuevo.")
            continue
        else:
            print("¡Fallaste!")
            tablero_oponente[fila][columna] = "🧊"
            tablero_visible[fila][columna] = "🧊"

        disparos_restantes -= 1

        # Verifica si se hundieron todos los barcos
        if disparos_acertados_jugador1 == cantidad_barcos:
            print("\n¡Felicidades Jugador 1! Hundiste todos los barcos del Jugador 2.")
            break
        if disparos_acertados_jugador2 == cantidad_barcos:
            print("\n¡Felicidades Jugador 2! Hundiste todos los barcos del Jugador 1.")
            break

        # Cambia el turno
        turno_jugador = 2 if turno_jugador == 1 else 1

    # Fin del juego
    print("\nEl juego termino.")
    print(f"Disparos acertados Jugador 1: {disparos_acertados_jugador1}")
    print(f"Disparos acertados Jugador 2: {disparos_acertados_jugador2}")
    print("\nTablero final Jugador 1:")
    imprimir_tablero(tablero_jugador1, revelar_barcos=True)
    print("\nTablero final Jugador 2:")
    imprimir_tablero(tablero_jugador2, revelar_barcos=True)

jugar()
