import bs4
import requests


def euribor_scraping():
    resultado = requests.get('https://www.expansion.com/mercados/euribor.html')
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
    valor = sopa.select('tbody tr td')[0]
    euribor = valor.getText()
    decimal = euribor.replace(',', '.')
    return float(decimal)




