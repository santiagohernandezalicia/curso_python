''' Clases para manejar la base de datos de películas '''
import csv
import os
import hashlib
from datetime import datetime

class Actor:
    ''' Clase para manejar la información de un actor '''
    def __init__(self, id_estrella, nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen, username):
        self.id_estrella       = id_estrella
        self.nombre            = nombre
        self.fecha_nacimiento  = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.url_imagen        = url_imagen
        self.username          = username
    
    def to_dict(self):
        ''' Devuelve un diccionario con la información del actor '''
        return {
            'id_estrella': self.id_estrella,
            'nombre': self.nombre,
            'fecha_nacimiento': self.fecha_nacimiento,
            'ciudad_nacimiento': self.ciudad_nacimiento,
            'url_imagen': self.url_imagen,
            'username': self.username
        }   

class pelicula:
    '''Clase para manejar la informacion de una pelicula'''
    def __init__(self, id_pelicula, titulo_pelicula, fecha_lanzamiento, url_poster):
        '''inicializa la clase con los datos de la pelicula'''
        self.id_pelicula    = id_pelicula
        self.titulo_pelicula = titulo_pelicula
        self.fecha_lanzamienti = datetime.strptime
        (fecha_nacimiento , "%Y-%m-%d").date()
        self.url_poster = url_poster

    def to_dict(self):
        '''devuelve un diccionario con la informacion de la pelicula'''
        return {
            'id_pelicula': self.id_pelicula,
            'titulo_pelicula': self.titulo_pelicula,
            'fecha_lanzamiento': self.fecha_lanzamiento.strftime 
            ("%Y-%m-%d"),
            'url_poster': self.url_poster
        }
    
class Relacion:
    '''Clase para manejar las relaciones entre actores y peliculas'''
    def __init__(self, id_relacion, id_pelicula, id_estrella, personaje):
        '''inicializa la clase con los datos de la relacion'''
        self.id_relacion = id_relacion
        self.id_estrella = id_estrella        
        self.id_pelicula = id_pelicula

    def to_dict(self):
        '''devuelve un diccionario con la informacion de la relacion'''
        return {
            'id_relacion': self.id_relacion,
            'id_estrella': self.id_estrella,
            'id_pelicula': self.id_pelicula,
            
        }

class User:
    '''clase para manejar la informacion de un usuario'''
    def __init__(self, username, nombre_completo, email, password, admin):
        self.username           = username
        self.nombre_completo    = nombre_completo
        self.email              = email
        self.password           = password
        self.admin              = admin

    def to_dict(self):
        '''devuelve un diccionario con la informacion del usuario'''
        return {
            'username': self.username,
            'nombre_completo': self.nombre_completo,
            'email': self.email,
            'password': self.password,
            'admin': self.admin
        }
    
    def hash_string(self, string):
        '''devuelve el hash de un string'''
        return hashlib.md5(string.encode()).hexdigest()
    
class SistemaCine:
    def __init__(self):
        '''inicializa el sistema de cine'''
        self.actores = {}
        self.peliculas = {}
        self.relaciones = {}
        self.usuarios = {}
    
    def cargar_csv(self, archivo, clase):
        '''carga los datos de un archivo csv en el sistema'''
        if clase == Actor:
            with open(archivo, encoding='utf-8') as f:
                reader = csv.DictReader(f)
            for row in reader:
                if clase == Actor:
                    actor = Actor(**row)
                    self.actores[actor.id_estrella] = actor
                elif clase == Pelicula:
                    pelicula = Pelicula(**row)
                    self.peliculas[pelicula.id_pelicula] = pelicula
                elif clase == Relacion:
                    relacion = Relacion(**row)
                    self.relaciones[relacion.id_relacion] = relacion
                elif clase == User:
                    user = User(**row)
                    self.usuarios[user.username] = user

if __name__ == '__main__':
    #archivo = "datos/actorees.csv"
    archivo_actores = "datos/movies_db - actores.csv"
    archivo_peliculas = "datos/movies_db - peliculas.csv"
    archivo_relaciones = "datos/movies_db - relaciones.csv"
    archivo_usuarios = "datos/movies_db - usuarios.csv"
    sistema= SistemaCine()
    sistema.cargar_csv(archivo_actores, Actor)
    sistema.cargar_csv(archivo_peliculas, Pelicula)
    sistema.cargar_csv(archivo_relaciones, Relacion)
    sistema.cargar_csv(archivo_usuarios, User)
    actores = sistema.actores
    for id_estrella, actor in actores.items():
       print(f"{id_estrella}: {actor.nombre:35s} - {actor.fecha_nacimiento}")
    
