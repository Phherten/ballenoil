from flask import Flask
from funciones import euribor_scraping

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


@app.route('/saluda')
def saluda():
    valor = euribor_scraping()
    return valor

