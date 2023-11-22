from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


def scraping(name):
    urlLOG = "https://tracker.gg/lol/profile/riot/BR/brayanlolv/overview?playlist=RANKED_SOLO_5x5".format(name)
    html = requests.get(urlLOG).content   
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())

    # trList =soup.find_all("tr")
    # print(trList)
    # teste = soup.find("div")
    # print(teste)
    return html

scraping("brayanlolv")








