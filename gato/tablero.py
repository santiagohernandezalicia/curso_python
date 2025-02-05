'''
Tablero.py: dibuja el tablero en el juego del gato
'''
import random

def dibuja_tablero(simbolos:dict):
    '''
    dibuja tablero'''
    print(f'''
        {simbolos ['1']} | {simbolos ['2']} | {simbolos ['3']} 
        -----------
        {simbolos ['4']} | {simbolos ['5']} | {simbolos ['6']}
        ----------
        {simbolos ['7']} | {simbolos ['8']} | {simbolos ['9']} 
        ''')
    
def ia(simbolos:dict):
    '''juega maquina'''
    ocupado = True
    while ocupado is True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X','O']:
            simbolos[x] = 'O'
            ocupado = False

def usuario(simbolos:dict):
    '''juega usuario'''
    ocupado = True
    lista_numeros= {str(x) for x in range(1,10)}
    while ocupado is True:
        x = input('Dame el numero de la casilla: ')
        if(x in lista_numeros):
          if simbolos[x] not in ['X','O']:
              simbolos[x] = 'X'
              ocupado = False
          else:
              print("casilla ocupada")
        else:
            print("Numero incorrecto")

def juego(simbolos:dict):
    '''juego'''
    lista_combinaciones=[
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['1','5','9'],
        ['3','5','7'],
        ['1','4','7'],
        ['2','5','8'],
        ['3','6','9']
    ]

    en_juego=True
    dibuja_tablero(simbolos)
    movimientos = 0
    gana = None
    while en_juego:
            usuario(simbolos)
            dibuja_tablero(simbolos)
            movimientos += 1
            gana = checa_winner(simbolos, lista_combinaciones)
            if gana is not None:
                en_juego = False
                continue
            if movimientos >= 9:
                en_juego = False
                continue
            ia(simbolos)
            dibuja_tablero(simbolos)
            movimientos += 1
            gana = checa_winner(simbolos, lista_combinaciones)
            if gana is not None:
                en_juego = False
                continue
            if movimientos >= 9:
                en_juego = False
                continue
    return gana



def checa_winner(simbolos:dict, combinaciones:list):
    '''checa ganador'''
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
            return simbolos[c[0]]
    return None


if __name__ == '__main__':
    numeros = {str(x) for x in range(1,10)}
    dsimbolos = {x:x for x in numeros}
    g = juego(dsimbolos)
    if g is None:
        print(f'Ganador: {g}')
    else:
        print('Empate')


    ''' 
    dibuja_tablero(dsimbolos)
    ia(dsimbolos)
    dibuja_tablero(dsimbolos)
    usuario(dsimbolos)
    dibuja_tablero(dsimbolos)

  
    x = random.choice(numeros)
    numeros.remove(x)
    dsimbolos[x] = 'X'
    dibuja_tablero(dsimbolos)
    o = random.choice(numeros)
    numeros.remove(O)
    dsimbolos[o] = 'O'
    dibuja_tablero(dsimbolos)
    print(numeros)
    '''
