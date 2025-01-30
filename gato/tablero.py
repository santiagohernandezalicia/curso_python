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


if __name__ == '__main__':
    numeros = {str(x) for x in range(1,10)}
    dsimbolos = {x:x for x in numeros}
    dibuja_tablero(dsimbolos)
    ia(dsimbolos)
    dibuja_tablero(dsimbolos)
    usuario(dsimbolos)
    dibuja_tablero(dsimbolos)

    ''' 
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
