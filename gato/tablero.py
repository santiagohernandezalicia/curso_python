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
    
def ia(simbolos:dict, lista_combinaciones:dict):
    '''juega maquina'''
    for x in simbolos.keys():
        if simbolos[x] not in ['X', 'O']:  # Si la casilla está vacía
            simbolos[x] = 'O'  # La IA coloca su "O"
            if checa_winner(simbolos, lista_combinaciones) == 'O':  # Si la IA gana, termina
                return
            simbolos[x] = x  # Deshacer la jugada si no gana

    # Aquí la IA intenta bloquear al usuario si está a punto de ganar
    for x in simbolos.keys():
        if simbolos[x] not in ['X', 'O']:  # Si la casilla está vacía
            simbolos[x] = 'X'  # Simula la jugada del usuario
            if checa_winner(simbolos, lista_combinaciones) == 'X':  # Si el usuario ganaría, la IA lo bloquea
                simbolos[x] = 'O'  # Coloca la "O" para bloquear
                return
            simbolos[x] = x  # Deshacer la jugada si no es necesario bloquear

    # Si el centro está libre, juega allí
    if simbolos["5"] == "5":
        simbolos["5"] = "O"
        return

    # Si el centro está ocupado, juega en una esquina
    esquinas = ['1', '3', '7', '9']
    for esquina in esquinas:
        if simbolos[esquina] == esquina:  # Si la esquina está libre
            simbolos[esquina] = 'O'
            return

    # Si no hay esquinas disponibles, juega en cualquier otro espacio libre
    for x in simbolos.keys():
        if simbolos[x] not in ['X', 'O']:
            simbolos[x] = 'O'
            return


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
            print("Elija un numero del 1 al 9")

def juego(simbolos:dict):
    '''juego del gato'''
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
    ia(simbolos, lista_combinaciones)

    en_juego = True
    dibuja_tablero(simbolos)
    movimientos = 0
    gana = None

    while en_juego:
        # Turno del usuario
        usuario(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1

        # Verificar si hay un ganador
        gana = checa_winner(simbolos, lista_combinaciones)
        if gana is not None:
            en_juego = False
            continue

        # Verificar empate (si las casillas están llenas)
        if movimientos >= 9:
            en_juego = False
            print("¡El juego terminó en empate!")
            continue

        # Turno de la IA
        ia(simbolos, lista_combinaciones)
        dibuja_tablero(simbolos)
        movimientos += 1

        # Verificar si hay un ganador después de la jugada de la IA
        gana = checa_winner(simbolos, lista_combinaciones)
        if gana is not None:
            en_juego = False
            continue
        
        # Verificar empate después del turno de la IA
        if movimientos >= 9:
            en_juego = False
            print("¡El juego terminó en empate!")
            continue

    return gana



def checa_winner(simbolos:dict, combinaciones:list):
    '''checa ganador'''
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
            return simbolos[c[0]]
    return None


def actualiza_score(score:dict,ganador:str):
    '''actualiza score'''
    X = score["X"]
    O = score["O"]
    if ganador is not None:
        print(f'El ganador es {ganador}')
        if ganador == 'X':
            X["G"] +=1
            O["P"] +=1
        elif ganador == 'O':
            O["G"] +=1
            X["P"] +=1
        else:
            X["E"] +=1
            O["E"] +=1
    else:
        print('Empate')
        X["E"] +=1
        O["E"] +=1

def despliega_tablero(score:dict):
    '''despliega el tablero'''
    print(f'''
    X | G:{score["X"]["G"]} | P:{score["X"]["P"]} | E:{score["X"]["E"]}
    O | G:{score["O"]["G"]} | P:{score["O"]["P"]} | E:{score["O"]["E"]}
    ''')

if __name__ == '__main__':
    numeros = {str(x) for x in range(1,10)}
    dsimbolos = {x:x for x in numeros}
    
    