"""
Introducción a Flask
https://parzibyte.me/blog
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return "<h1>Hola mundo con Flask.</h1><br>\n<h2>Autor: @vysery98</h2>"

@app.route('/suma')
def suma():

    resultado1 = 10 + 10
    resultado2 = 20 + 20

    return "<h3>10 + 10 = %d</h3>\n<h3>20 + 20 = %d</h3>" % (resultado1, resultado2)

@app.route('/listado')
def listado():

    salida = ""
    lista = ["Ingeniería Civil", "Geología", "Artes Visuales", "Tecnologías de la Información", "Arqu" + 
    "itectura", "Computación", "Artes Escénicas", "Telecomunicaciones", "Geología"]

    for i in range(len(lista)):
        salida += ("\n\t<li>" + lista[i] + "</li>")

    return "<h1><b>Carreas del Área Técnica:</b></h1>\n<h2><ul>%s\n</ul></h2>" % (salida)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
