import os
import requests
import json
import time
from tkinter import *


def cotacao():

    moedas = open("cryptoMoedas.txt",'r')
    cryptos = []

    vezes = int(input("Quantas vezes vai ler: "))
    delay = int(input("Tempo entre as leituras: "))

    for i in moedas:
        cryptos.append(i.strip())

    for i in range(vezes):
        cotacoes = capturarCotacao(cryptos)
        listarCotacoes(cotacoes)
        print('')

        if i != vezes-1:
            time.sleep(delay)

    moedas.close()

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