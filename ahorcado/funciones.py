'''funciones auxiliares'''
import string
import unicodedata 
from random import choice

def carga_archivo_texto(archivo:str)->list:
    '''carga el archivo de texto y devuelve
     una lista con las oraciones del archivo'''
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones

def carga_plantillas(nombre_plantilla)->dict:
    ''''carga plantiilas del juego a partir de un archivo de texto'''
    plantillas={}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'./plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas

def despliega_plantilla(diccionario:dict, nivel:int):
    '''despliega la plantilla del juego'''
    if nivel <=5:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)

def obten_palabras(lista:list)->list:
    texto =' '.join(lista[120])
    palabras = texto.split()
    #convertimos a minusculas
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    #removemos signos de puntuacion y caracteres especiales
    set_palabras ={palabra.strip(string.punctuation) for palabra in 
    set_palabras}
    #removemos numeros, parentesis, corchetes y otros caracteres
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}
    #remover acentos
    set_palabras = {unicodedata.normalize('NFKD', palabra).encode
    ('ascii','ignore').decode('ascii') for palabra in set_palabras}
    return list(set_palabras)


def adivina_letra(abc:dict, palabra:str, letras_adivinas:set,turnos:int)->int:
    '''adivina una letra de la palabra'''
    palabra_oculta = ""
    for letra in palabra:
        if letra in letras_adivinas:
            palabra_oculta += letra
        else:
            palabra_oculta += '_'
    print(f'tienes {turnos} de fallar')
    abcd= ''.join(abc.values())
    print(f'el abecedario es: {abc}')
    print(f'palabra: {palabra_oculta}')
    letra = input('ingresa una letra: ')
    letra = letra.lower()
    if len(letra) != 1 or letra not in abc:
        print('ingresa una letra valida')
    else:
        if abc[letra] == "*":
            print('ya habias ingresado esta letra')
        if letra in palabra:
            letras_adivinas.add(letra)
        else:
            turnos -= 1
    return turnos


if __name__ == "__main__":
    plantilla = carga_plantillas('plantilla')
    despliega_plantilla(plantilla,5)
    lista_oraciones = carga_archivo_texto('./datos/pg15532.txt')
    lista_palabras = obten_palabras(lista_oraciones)
    print(len(lista_palabras))
    p = choice(lista_palabras)
    print(p)    
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    t = 5
    t = adivina_letra(abcdario, p , adivinadas, t)
    print(t)
    t = adivina_letra(abcdario, p , adivinadas, t)
    print(t)