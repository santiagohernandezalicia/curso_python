'''programa principal de libros web'''
from flask import Flask, render_template, request
import funciones as fn

app = Flask(__name__)

archivo_csv = 'booklist2000.csv'
lista_libros = fn.lee_archivo_csv(archivo_csv)
diccionario_titulos = fn.crea_diccionario(lista_libros,'title')
diccionario_autores = fn.crea_diccionario(lista_libros,'author')

@app.route('/')
def inicio():
    '''pagina de inicio de la aplicaion'''
    return render_template('index.html')

@app.route('/titulo', methods=['GET','POST'])
def busqueda_titulo():
    '''busca un libro por el titulo'''
    resultado=[]
    if request.method == 'POST':
        titulo = request.form['titulo']
        resultado = fn.busca_en_diccionario(diccionario_titulos, titulo)
        print(titulo)
        print(resultado)
    return render_template('titulo.html', lista_libros=resultado)

if __name__ == '__main__':
    app.run(debug=True)
