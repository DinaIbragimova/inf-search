import requests
from bs4 import BeautifulSoup

def parsePage(url, index):
    file = open(f'startAndroid{index}.txt', 'w')
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    title = soup.find('h1', attrs={"class": "article-title"}).text.strip()
    publishedDateTime = soup.find('dd', attrs={"class": "published hasTooltip"}).find("time").text.strip()
    file.write(title + "\n")
    file.write(publishedDateTime + "\n")
    articleContent = soup.find('section', attrs={"class": "article-content"})
    for content in articleContent.find_all(['p', 'h3']):
        file.write(content.text.strip() + "\n")
    file.close()
