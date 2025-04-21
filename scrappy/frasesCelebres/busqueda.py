import csv
import argparse
'''programa para buscar una palabra dentro de frases.csv'''
def buscar_palabra(frase:str, palabra:str)->bool:
    '''busca una palabra dentro de una frase'''
    if palabra in frase:
        return True
    else:
        return False

def main():
    '''funcion principal'''
    parser = argparse.ArgumentParser(description='Buscar una palabra en frases.csv')
    parser.add_argument('palabra', type=str, help='Palabra a buscar')
    args = parser.parse_args()
    palabra = args.palabra
    #abrimos el archivo csv
    with open('frases.csv', 'r') as f:
        #leemos el archivo csv
        lineas = f.readlines()
        #buscamos la palabra en cada linea
        for linea in lineas:
            if buscar_palabra(linea, palabra):
                print(linea)
