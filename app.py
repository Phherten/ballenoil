from flask import Flask, request
from funciones import devolver_variables, agregar_datos
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def agregar():  # put application's code here
    request_body = request.get_json()
    agregar_datos(request_body['km'])


@app.route('/km')
def km():
    valor = devolver_variables()
    return valor


if __name__ == '__main__':
    app.run()
