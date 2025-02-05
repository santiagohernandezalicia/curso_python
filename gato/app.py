import tablero

def main():
    '''
    funcion principal
    '''
    numeros = {str(x) for x in range(1,10)}
    dsimbolos = {x:x for x in numeros}
    g = tablero.juego(dsimbolos)
    if g is not None:
        print(f'ganador: {g}')
    else:
        print('empate')