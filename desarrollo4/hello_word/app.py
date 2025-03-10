from flask import Flask
app = Flask(__name__)
@app.route("/") # home or root of website 
def index():
    return '''<html>
                    <head>
                            <title>HELLO WORLD</title>
                    </head>
                    <body><h1>Hello word</h1>
                        <p>Ir a la pagina <a href="/about">Acerca de</a></p>
                    </body>
            </html>'''


            
@app.route("/about") # info about the site
def about():
    return '''<html>
                <head>
                    <title>About this page</title>
                </head>
                <body><h1>Acerca de</h1>
                    <p>Ir a la pagina de <a href="/">Inicia</a></p>
                </body>
            </html>'''

if __name__ == "__main__":
    app.run(debug=True)
    