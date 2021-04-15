"""
Introducción a Flask
https://parzibyte.me/blog
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return "<h1>Hola mundo con Flask</h1>"

@app.route('/suma')
def suma():
    resultado = 5 + 5
    return "<h1>5 + 5 = {}</h1>".format(resultado)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
