'''archivo con las funciones necesarias de la la aplicacion Libro web'''
import csv

def leer_archivo_csv(archivo:str)->list:
    '''lee un archivo csv y retorna una lista de diccionarios'''
    with open(archivo, "r", recording="utf-8") as f:
        return [x for x in csv.DictReader(f)]

def crea_diccionario_titulos(lista:list) -> dict:
    '''crea un diccionario con los titulos de los libros como clave y el resto de 
    datos como valor'''
    return {x["Titulo"]:x for x in lista}

if __name__ == '__main__':
    archivo_csv = 'booklist2000.csv'
    lista_libros = leer_archivo_csv(archivo_csv)
    diccionario_libros = crea_diccionario_titulos(lista_libros)
