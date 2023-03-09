import requests
from bs4 import BeautifulSoup

from parser import parsePage

mainUrl = "https://startandroid.ru/ru/uroki/vse-uroki-spiskom.html"
r = requests.get(mainUrl)
soup = BeautifulSoup(r.content, 'html5lib')
urls = []

table = soup.find('tbody')
for row in table.findAll('tr'):
    link = "https://startandroid.ru" + row.find('a')['href']
    urls.append(link)

file = open('index.txt', 'w')
for i in range(100):
    parsePage(urls[i], i)
    file.write(f"{urls[i]}, startAndroid{i}.txt" + "\n")
file.close()
