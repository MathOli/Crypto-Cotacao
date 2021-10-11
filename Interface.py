import os
import requests
import json
import time
from tkinter import *


def cotacao():

    delay = inputTime.get()
    vezes = inputRead.get()

    # print(f'Repetições {inputRead.get()}')
    # print(f'Delay {inputTime.get()}s')

    moedas = open("cryptoMoedas.txt",'r')
    cryptos = []

    # vezes = int(input("Quantas vezes vai ler: "))
    # delay = int(input("Tempo entre as leituras: "))

    textoTime = f'{delay}s de Intervalo'
    textoRepeticao = f'{vezes} Leitura(s)'
    readRepet["text"] = textoRepeticao
    readTime["text"] = textoTime

    for i in moedas:
        cryptos.append(i.strip())

    for i in range(int(vezes)):
        readCotacao["text"] = capturarCotacao(cryptos)
        # readCotacao["text"] = listarCotacoes(cotacoes)
        time.sleep(int(delay))
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
    leituras = []
    for crypto in cotacoes:
        leituras.append(f"Crypto {crypto['Crypto'].upper()} : R$ {crypto['BRL']:.2f}")
    return leituras

window = Tk()

window.title("Cotações de Crypto Moedas")
window.geometry("500x500")
window.config(background="#bab8b5")

textRead = Label(window, text="Quantidade de Leitura",background="#bab8b5")
textRead.pack()
inputRead = Entry(window)
inputRead.pack()

textTime = Label(window, text="Intervalo das Leituras",background="#bab8b5")
textTime.pack()
inputTime = Entry(window)
inputTime.pack()

buttonCotacao = Button(window,text="imprimir", command=cotacao)
buttonCotacao.pack()

readRepet = Label(window,text="",background="#bab8b5")
readRepet.pack()
readTime = Label(window,text="",background="#bab8b5")
readTime.pack()
readCotacao = Label(window,text="",background="#bab8b5")
readCotacao.pack()


window.mainloop()