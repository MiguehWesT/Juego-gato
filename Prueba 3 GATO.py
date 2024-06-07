import random

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)

def verificar_ganador(tablero, jugador):
    for fila in tablero:
        if fila.count(jugador) == 3:
            return True
    for col in range(3):
        if [fila[col] for fila in tablero].count(jugador) == 3:
            return True
    if [tablero[i][i] for i in range(3)].count(jugador) == 3 or [tablero[i][2-i] for i in range(3)].count(jugador) == 3:
        return True
    return False

def movimiento_jugador(tablero, jugador):
    while True:
        fila = int(input(f"Jugador {jugador}, elige una fila (1-3): ")) - 1
        col = int(input(f"Jugador {jugador}, elige una columna (1-3): ")) - 1
        if 0 <= fila <= 2 and 0 <= col <= 2 and tablero[fila][col] == " ":
            tablero[fila][col] = jugador
            break
        else:
            print("Movimiento inválido, intenta de nuevo.")

def movimiento_maquina(tablero):
    while True:
        fila, col = random.randint(0, 2), random.randint(0, 2)
        if tablero[fila][col] == " ":
            tablero[fila][col] = "O"
            break

def juego_gato():
    print("Bienvenido al GATO")

    while True:
        tablero = [[" " for _ in range(3)] for _ in range(3)]
        jugador_actual = "X"
        juego_terminado = False

        print("\nMenu:")
        print("1. Nueva partida, Jugador 1 vs Maquina")
        print("2. Nueva partida, Jugador 1 vs Jugador 2")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            while not juego_terminado:
                imprimir_tablero(tablero)
                movimiento_jugador(tablero, jugador_actual)
                if verificar_ganador(tablero, jugador_actual):
                    imprimir_tablero(tablero)
                    print(f"¡Felicidades, Jugador {jugador_actual} has ganado!")
                    juego_terminado = True
                elif " " not in sum(tablero, []):
                    imprimir_tablero(tablero)
                    print("¡Es un empate!")
                    juego_terminado = True
                else:
                    jugador_actual = "O" if jugador_actual == "X" else "X"
                    movimiento_maquina(tablero)
                    if verificar_ganador(tablero, jugador_actual):
                        imprimir_tablero(tablero)
                        print(f"¡La máquina ha ganado! Lo siento, Jugador {jugador_actual}.")
                        juego_terminado = True
                    elif " " not in sum(tablero, []):
                        imprimir_tablero(tablero)
                        print("¡Es un empate!")
                        juego_terminado = True
                    jugador_actual = "X"
        elif opcion == "2":
            while not juego_terminado:
                imprimir_tablero(tablero)
                movimiento_jugador(tablero, jugador_actual)
                if verificar_ganador(tablero, jugador_actual):
                    imprimir_tablero(tablero)
                    print(f"¡Felicidades, Jugador {jugador_actual} has ganado!")
                    juego_terminado = True
                elif " " not in sum(tablero, []):
                    imprimir_tablero(tablero)
                    print("¡Es un empate!")
                    juego_terminado = True
                else:
                    jugador_actual = "O" if jugador_actual == "X" else "X"
        elif opcion == "3":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Iniciar el juego
juego_gato()
