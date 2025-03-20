''' Clases para manejar la base de datos de películas '''
import csv
import os
import hashlib
from datetime import datetime

class Actor:
    ''' Clase para manejar la información de un actor '''
    def __init__(self, id_estrella, nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen, username):
        self.id_estrella       = int(id_estrella)
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

class Pelicula:
    ''' Clase para manejar la información de una película '''
    def __init__(self, id_pelicula, titulo_pelicula, fecha_lanzamiento, url_poster):
        ''' Inicializa la clase con los datos de la película '''
        self.id_pelicula       = int(id_pelicula)
        self.titulo_pelicula   = titulo_pelicula
        self.fecha_lanzamiento = datetime.strptime(fecha_lanzamiento, "%Y-%m-%d").date()
        self.url_poster        = url_poster
    def to_dict(self):
        ''' Devuelve un diccionario con la información de la película '''
        return {
            'id_pelicula': self.id_pelicula,
            'titulo_pelicula': self.titulo_pelicula,
            'fecha_lanzamiento': self.fecha_lanzamiento.strftime("%Y-%m-%d"),
            'url_poster': self.url_poster
        }
    
    #clase string para imprimir la información de la película
    def __str__(self):
        ''' Devuelve un string con la información de la película '''
        return f"{self.titulo_pelicula} ({self.fecha_lanzamiento.year})"


class Relacion:
    ''' Clase para manejar la relación entre actores y películas '''
    def __init__(self, id_relacion, id_estrella, id_pelicula):
        ''' Inicializa la clase con los datos de la relación '''
        self.id_relacion = int(id_relacion)
        self.id_estrella = int(id_estrella)
        self.id_pelicula = int(id_pelicula)
        
    def to_dict(self):
        ''' Devuelve un diccionario con la información de la relación '''
        return {
            'id_relacion': self.id_relacion,
            'id_estrella': self.id_estrella,
            'id_pelicula': self.id_pelicula,
        }

class User:
    ''' Clase para manejar la información de un usuario '''
    def __init__(self, username, nombre_completo, email, password):
        ''' Inicializa la clase con los datos del usuario '''
        self.username        = username
        self.nombre_completo = nombre_completo
        self.email           = email
        self.password        = password
    
    def to_dict(self):
        ''' Devuelve un diccionario con la información del usuario '''
        return {
            'username': self.username,
            'nombre_completo': self.nombre_completo,
            'email': self.email,
            'password': self.password,
            'admin': self.admin
        }
    
    def hash_string(self, string):
        ''' Devuelve el hash de un string '''
        return hashlib.sha256(string.encode()).hexdigest()

class SistemaCine:
    ''' Clase para manejar la base de datos de películas '''
    def __init__(self):
        ''' Inicializa la clase con los datos de la base de datos '''
        self.actores = {}
        self.peliculas = {}
        self.relaciones = {}
        self.usuarios = {}
        self.idx_actor = 0
        self.idx_pelicula = 0
        self.idx_relacion = 0
        self.usuario_actual = None

    def cargar_csv(self, archivo, clase):
        ''' Carga los datos de un archivo CSV en la base de datos'''
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
        if clase ==Actor:
            self.idx_actor = max(self.actores.keys()) if self.actores else 0
        elif clase == Pelicula:
            self.idx_pelicula = max(self.peliculas.keys()) if self.peliculas else 0
        elif clase == Relacion:
            self.idx_relacion = max(self.relaciones.keys()) if self.relaciones else 0

    def obtener_peliculas_por_actor(self, id_estrella):
        ''''devuelve una lista de peliculas en las que ha participado un actor'''
        id_peliculas = [rel.id_pelicula for rel in self.relaciones.values() if rel.id_estrella == id_estrella]
        return [self.peliculas[id_pelicula] for id_pelicula in id_peliculas]

    def obtener_actores_por_pelicula(self, id_pelicula):
        '''devuelve una lista de actores que han participado en una película'''
        id_actores = [rel.id_estrella for rel in self.relaciones.values() if rel.id_pelicula == id_pelicula]
        return [self.actores[id_estrella] for id_estrella in id_actores]
    
    def login(self, username, password):
        ''' Verifica si un usuario puede iniciar sesión '''
        if username in self.usuarios:
            user = self.usuarios[username]
            if user.hash_string(password) == user.password:
                self.usuario_actual = user
                return True
        return False

if __name__ == '__main__':
    #archivo = "datos/actores.csv"
    archivo_actores = "datos/movies_db - actores.csv"
    archivo_peliculas = "datos/movies_db - peliculas.csv"
    archivo_relaciones = "datos/movies_db - relacion.csv"
    archivo_usuarios = "datos/movies_db - users.csv"
    sistema = SistemaCine()
    sistema.cargar_csv(archivo_actores, Actor)
    sistema.cargar_csv(archivo_peliculas, Pelicula)
    sistema.cargar_csv(archivo_relaciones, Relacion)    
    sistema.cargar_csv(archivo_usuarios, User)
    actores = sistema.actores
    for id_estrella, actor in actores.items():
        print(f"{id_estrella}: {actor.nombre:35s} - {actor.fecha_nacimiento}")
    lista_peliculas = sistema.obtener_peliculas_por_actor(1)
    for pelicula in lista_peliculas:
        print(pelicula)
        print(len(lista_peliculas))
    lista_actores = sistema.obtener_actores_por_pelicula(1)
    for actor in lista_actores:
        print(actor.nombre)
        print(len(lista_actores))
    
    u = sistema.usuarios['fcirettg']
    print(type(u))
    print(u.username)
    print(u.password)
    print(u.hash_string(u.password))
    exito = sistema.login('fcirettg', '12345')
    print(exito)
    print(sistema.usuario_actual.username)
