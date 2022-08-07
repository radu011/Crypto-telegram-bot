import requests
import json
from yhFinanceKey import headers

def getCryptoInfos(tag):
    url = "https://yh-finance.p.rapidapi.com/market/v2/get-quotes"

    tag += "-USD"
    querystring = {"region":"US,BR,AU,CA,FR,DE,HK,IN,IT,ES,GB,SG","symbols":tag}

    response = requests.request("GET", url, headers=headers, params=querystring)

    final = "  ### " + tag + " ###" + "\n"

    data = response.json()
    y = json.dumps(data)
    x = json.loads(y)

    if str(x.get("quoteResponse")) == "{'result': [], 'error': None}":
        return "No data found"

    info = x.get("quoteResponse").get("result")[0]
    regMarketPrice = info.get("regularMarketPrice")
    final += "Price: " + str(regMarketPrice) + "\n"
    regMarketChangePer = info.get("regularMarketChangePercent")
    final += "Change Percent: " + str("{:.2f}".format(regMarketChangePer)) + "%" + "\n"
    regMarketDayLow = info.get("regularMarketDayLow")
    final += "Day Low: " + str(regMarketDayLow) + "\n"
    regMarketDayHigh = info.get("regularMarketDayHigh")
    final += "Day High: " + str(regMarketDayHigh) + "\n"
    regMarketVolume = info.get("regularMarketVolume")
    final += "Volume: " + str(regMarketVolume) + "\n"

    return final

def getNews(tag = "crypto"):
    url = "https://yh-finance.p.rapidapi.com/news/v2/list"

    querystring = {"region":"US","snippetCount":"10","s":tag}

    payload = "\"Pass in the value of uuids field returned right in this endpoint to load the next page, or leave empty to load first page\""

    response = requests.request("NEWS", url, data=payload, headers=headers, params=querystring)

    data = response.json()
    y = json.dumps(data)
    x = json.loads(y)
    print(data)
