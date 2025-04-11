def jugar():
    """
    Función principal del juego.
    """
    print("¡Bienvenido a Batalla Naval!")

    # Solicitar tamaño del tablero y cantidad de barcos
    while True:
        try:
            tamano_tablero = int(input("Ingrese el tamaño del tablero (por ejemplo, 10 para un tablero 10x10): "))
            if tamano_tablero <= 0:
                print("El tamaño del tablero debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    while True:
        try:
            cantidad_barcos = int(input(f"Ingrese la cantidad de barcos (máximo {tamano_tablero * tamano_tablero}): "))
            if cantidad_barcos <= 0 or cantidad_barcos > tamano_tablero * tamano_tablero:
                print(f"La cantidad de barcos debe estar entre 1 y {tamano_tablero * tamano_tablero}.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    cantidad_disparos = cantidad_barcos * 2  # Por ejemplo, permitir el doble de la cantidad de barcos

    print(f"\nEl tablero es de tamaño {tamano_tablero}x{tamano_tablero}.")
    print(f"Hay {cantidad_barcos} barcos escondidos.")
    print(f"Tenes {cantidad_disparos} disparos para encontrarlos.\n")

    # Crear el tablero y colocar los barcos
        tablero = crear_tablero(tamano_tablero)
        colocar_barcos(tablero, cantidad_barcos)
    
    def colocar_barcos(tablero, cantidad):
        """
        Coloca una cantidad de barcos aleatoriamente en el tablero.
        """
        import random
        tamano = len(tablero)
        barcos_colocados = 0
        while barcos_colocados < cantidad:
            fila = random.randint(0, tamano - 1)
            columna = random.randint(0, tamano - 1)
            if not tablero[fila][columna]:
                tablero[fila][columna] = True
                barcos_colocados += 1
    def crear_tablero(tamano):
        """
        Crea un tablero vacío de tamaño tamano x tamano.
        """
        return [[False for _ in range(tamano)] for _ in range(tamano)]
    colocar_barcos(tablero, cantidad_barcos)

    disparos_restantes = cantidad_disparos
    disparos_acertados = 0
    disparos_fallados = 0

    while disparos_restantes > 0:
        imprimir_tablero(tablero)
        print(f"\nDisparos restantes: {disparos_restantes}")
        try:
            fila = int(input(f"Ingrese la fila (0-{tamano_tablero-1}): "))
            columna = int(input(f"Ingrese la columna (0-{tamano_tablero-1}): "))
        except ValueError:
            print("Por favor, ingrese números válidos.")
            continue

        # Validar coordenadas
        if fila < 0 or fila >= tamano_tablero or columna < 0 or columna >= tamano_tablero:
            print("¡Coordenadas fuera de rango! Intenta de nuevo.")
            continue

        # Verificar el disparo
        if tablero[fila][columna] is True:
            print("¡Acertaste! Hundiste un barco.")
            tablero[fila][columna] = "X"  # Marcar como barco hundido
            disparos_acertados += 1
        elif tablero[fila][columna] in ["X", "O"]:
            print("Ya disparaste en esta posición. Intenta de nuevo.")
        imprimir_tablero(tablero, revelar_barcos=True)
        else:
            print("¡Fallaste!")
            tablero[fila][columna] = "O"  # Marcar como disparo fallido
            disparos_fallados += 1

        disparos_restantes -= 1

        # Verificar si se hundieron todos los barcos
        if disparos_acertados == cantidad_barcos:
            print("\n¡Felicidades! Hundiste todos los barcos.")
            break

    # Fin del juego
    print("\n¡Juego terminado!")
    print(f"Disparos acertados: {disparos_acertados}")
    print(f"Disparos fallados: {disparos_fallados}")

    # Mostrar la posición de todos los barcos
    print("\nPosiciones de todos los barcos:")
        imprimir_tablero(tablero, revelar_barcos=True)
    
    def imprimir_tablero(tablero, revelar_barcos=False):
        """
        Función para imprimir el tablero.
        Si revelar_barcos es True, muestra la posición de los barcos.
        """
        for fila in tablero:
            for celda in fila:
                if celda is True and not revelar_barcos:
                    print("~", end=" ")  # Ocultar barcos
                elif celda is True and revelar_barcos:
                    print("B", end=" ")  # Mostrar barcos
                else:
                    print(celda, end=" ")
            print()
