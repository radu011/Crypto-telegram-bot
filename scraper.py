from bs4 import BeautifulSoup
import requests

def getNews():
    page_url = 'https://www.businesstoday.in/crypto'

    webpage = requests.get(page_url)

    trav = BeautifulSoup(webpage.content, 'html.parser')

    M = 1

    finalData = ""
    for link in trav.find_all('a'):
        if(str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
                    and len(link.string) > 35):

            if M != 1:
                finalData += "\n"
            finalData += str(M) + ". " + link.string + " (" + link.get("href") + ")"
            M += 1
    
    return finalData

def getAbrev():
    finalData = ""

    page_url = 'https://www.binance.com/en/markets'

    webpage = requests.get(page_url)

    trav = BeautifulSoup(webpage.content, 'html.parser')

    main = trav.find('div', {'class': 'css-1vuj9rf'})

    abrevs = main.find_all('div', {'class': 'css-1x8dg53'})
    names = main.find_all('div', {'class': 'css-1ap5wc6'})

    dict = {}

    for i in range(len(abrevs)):
        dict[names[i].string] = abrevs[i].string
    
    for item in dict:
        finalData += item + ": " + dict[item] + "\n"
    finalData = finalData[:-1]

    return finalData
