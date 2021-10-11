import requests
import json
import time




def cotacao():
    moedas = ["binancecoin", "coinary-token", "ripple", "smooth-love-potion", "dogecoin", "contentos"]


    for i in range(3):
        cotacoes = capturarCotacao(moedas)
        listarCotacoes(cotacoes)
        time.sleep(5)
        print(' ')

def capturarCotacao(moedas):
    cotacoes = []
    for moeda in moedas:
        cotacao = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={moeda}&vs_currencies=brl")
        cotacao = cotacao.json()
        cotacao = {"Crypto": moeda, "BRL": cotacao[moeda]['brl']}
        cotacoes.append(cotacao)

    return cotacoes
def listarCotacoes(cotacoes):

    for crypto in cotacoes:
        print(f"Crypto {crypto['Crypto'].upper()} : R$ {crypto['BRL']:.2f}")


if __name__ == "__main__":
    cotacao()