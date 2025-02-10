'''funciones auxiliares'''

def carga_archivo_texto(archivo:str)->list:
    '''carga el archivo de texto y devuelve
     una lista con las oraciones del archivo'''
    with open(archivo, "r") as file:
        oraciones = file.readlines()
    return oraciones

if __name__ == "__main__":
    lista = carga_archivo_texto('./platillas/plantillas-0.txt')
    for elmento in lista:
        print(elmento)