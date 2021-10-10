import requests
import json

moedas = ["binancecoin","coinary-token","ripple","smooth-love-potion","dogecoin","contentos"]
cotacoes = []

for moeda in moedas:
    cotacao = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={moeda}&vs_currencies=brl")
    cotacao = cotacao.json()
    cotacao = {"Crypto": moeda, "BRL" : cotacao[moeda]['brl'] }
    cotacoes.append(cotacao)

for crypto in cotacoes:
    print(f"Crypto {crypto['Crypto'].upper()} : R$ {crypto['BRL']:.2f}")