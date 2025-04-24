'''programa que busca una lista de palabras en las frases celebres de peiculas'''
import csv 
import os
import argparse

#funcion para leer el archivo csv y cargar las frases en una lista de diccionarios
def leer_csv(archivo):
    frases = []
    with open(archivo,'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        for fila in lector:
            frases.append(fila[0])
    return frases

# Funcion para buscar palabras en las frases
def buscar_palabras(frases, palabras):
    '''busca una lista de palabras en una lista'''
    frases_encontradas = []
    for frase in frases:
        for palabra in palabras:
            if palabra.lower() in frase.lower():
                frases_encontradas.append(frase)
                break
    return frases_encontradas
    

# Funcion para mostrar las frases encontradas
def mostrar_frases(frases):
    '''busca una lista de palabras en una lista'''
    for frase in frases:
        print(frase)

# funcion principal 
def main(archivo, lista_palabras):
    '''busca una lista de palabras en una lista'''
    #leer el archivo csv y cargar las frases en una lista de diccionarios
    frases = leer_csv(archivo)
    #buscar las palabras en las frases
    frases_encontradas = buscar_palabras(frases, lista_palabras)
    #mostrar las frases encontradas
    mostrar_frases(frases_encontradas)




if __name__== '__main__':
    #crear parser 
    parser = argparse.ArgumentParser(description='Buscar frases de en frases celebres de peliculas .')

    #añadir argumentos
    parser.add_argument('palabras', nargs='+', help='Lista de palabras a buscar en las frases.')
    #parsear los documentos
    args= parser.parse_args()
    archivo_frases = os.path.join(os.path.dirname(__file__), 'frases.csv')
    #llamar a la funcion principal
    main(archivo_frases, args.palabras)

    print(f'Frases encontradas: {len(args.palabras)}')
    