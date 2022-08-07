from bs4 import BeautifulSoup
import requests

def getTop():
    ### Get URL
    url = "https://coinmarketcap.com"
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")

    ### Get info from html code
    tbody = doc.tbody
    trs = tbody.contents

    names = []
    prices = []

    for tr in trs[:10]:
        name, price = tr.contents[2:4]
        cryptoName = name.p.string
        cryptoPrice = price.a.string

        names.append(cryptoName)
        prices.append(cryptoPrice)

    data = " ### Top 10 Cryptocurrencies ### \n"
    for index in range(len(names)):
        if index != 0:
            data += "\n"
        data += "   " + str(index + 1) + ". " + names[index] + ": " + prices[index]

    return data