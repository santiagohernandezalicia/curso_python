'''programa que busca una lista de palabras en las frases celebres de peiculas'''
import csv 
import os
import argparse
import Levenshtein

#funcion para leer el archivo csv y cargar las frases en una lista de diccionarios
def leer_csv(archivo):
    frases = []
    with open(archivo,'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        for fila in lector:
            frases.append([fila[0],fila[1]])
    return frases

# Funcion para buscar palabras en las frases
def buscar_palabras(frases:list, frases_a_buscar:str)->list:
    '''busca una lista de palabras en una lista'''
    frases_encontradas = []
    frases_a_buscar = frases_a_buscar.lower()
    for lista in frases: #lista contiene la frase y pelicula
        frase = lista[0]
        pelicula = lista[1]
        ratio = Levenshtein.ratio(frase, frases_a_buscar)
        #if ratio > 0.8: #si la distancia es menor a 0.8, se considera una coincidencia
        frases_encontradas.append([frase,pelicula,ratio])
    return frases_encontradas 
    

# Funcion para mostrar las frases encontradas
def mostrar_frases(frases:list, porcentaje:float=0.8)->None:
    '''busca una lista de palabras en una lista'''
    for lista in frases:
        frase = lista[0]
        pelicula = lista[1]
        ratio = lista[2]
        if ratio >= porcentaje:
            print(f"({frase}) - {pelicula} - Ratio: {ratio:.2f}")
        

# funcion principal 
def main(archivo, una_frase:str, tasa:float)->None:
    '''busca una lista de palabras en una lista'''
    #leer el archivo csv y cargar las frases en una lista de diccionarios
    frases = leer_csv(archivo)
    #buscar las palabras en las frases
    frases_encontradas = buscar_palabras(frases, una_frase)
    #dsplegar la frase a encontrar
    print(f"Buscando la frase: {una_frase}")
    #mostrar las frases encontradas
    mostrar_frases(frases_encontradas,tasa)




if __name__== '__main__':
    #crear parser 
    parser = argparse.ArgumentParser(description='Buscar frases de en frases celebres de peliculas .')
    #añadir argumentos
    parser.add_argument('frase', help='Frase a buscar.')
    parser.add_argument('--porcentaje', type=float, default =0.8, help='Porcentaje de coincidencia default: 0.8')
    #parsear los documentos
    args= parser.parse_args()
    archivo_frases = os.path.join(os.path.dirname(__file__), 'frases_consolidadas.csv')
    #llamar a la funcion principal
    main(archivo_frases, args.frase, args.porcentaje)
    #main(archivo_frases, "el futuro no esta escrito")

   
    