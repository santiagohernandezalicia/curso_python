'''
programa principal del juego ahorcado
'''
import os
import unicodedata
import argparse
import string
from random import choice
import funciones as fn

def main(archivo_texto:str,nombre_plantilla='plantilla'):
    '''
    programa principal
    '''
    #cargamos plantillas
    plantillas = fn.carga_plantillas(nombre_plantilla)
    lista_oraciones = fn.carga_archivo_texto(archivo_texto)
    palabras = fn.obten_palabras(lista_oraciones)
    
    o = 5 #oportunidades
    p = choice(palabras)
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    while o > 0:
        fn.despliega_plantilla(plantillas,o)
        o =  fn.adivina_letra(abcdario, p, adivinadas, o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('Felicitaciones, adivinaste la palabra')
            break
    fn.despliega_plantilla(plantillas,o)
    print(f'la palabra era: {p}')

 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Juego del ahorcado') 
    parser.add_argument('archivo', help='archivo de texto con palabras', default='./datos/pg15532.txt')
    args = parser.parse_args()
    archivo = args.archivo
    if os.stat(archivo)== False:
        print('archivo vacio')
        exit()
    main(archivo)
    #archivo = './datos/pg15532.txt'
    