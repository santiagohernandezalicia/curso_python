import tablero

def main():
    '''funcion principal'''
    nombre_usuario = input('Nombre de usuario: ').strip() or "usuario"

    X = {"G":0,"P":0,"E":0}
    O = {"G":0,"P":0,"E":0}
    score ={"X":X,"O":O}
    numeros = [str(i) for i in range(1,10)]
    corriendo= True
    while corriendo:
        print(f"\nTurno de {nombre_usuario} (X)")
        dsimbolos = {x:x for x in numeros}
        g = tablero.juego(dsimbolos)
        if g == "X":
            print(f"{nombre_usuario} ha ganado (X)")
        elif g == "O":
            print("Gano la computadora.")
        else:
            print("Empate")

        tablero.actualiza_score(score,g)
        tablero.despliega_tablero(score)

        seguir = input('Quieres seguir jugando? (s/n): ')
        if seguir.lower() == 'n':
            corriendo = False


if __name__ == '__main__':
    main()