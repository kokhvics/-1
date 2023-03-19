from bs4 import BeautifulSoup
import requests

def parse():
    url=''
    try:
        url = 'https://www.omgtu.ru/l/?rss=y&SHOWALL_1=1'
    except:
        print('Подключение недоступно')

    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")

    block = soup.findAll('div', class_='news__item')

    zagolovok = []
    for data in block:
        zag = data.find('h3',class_='news-card__title')
        if zag is not None:
            zagolovok.append(zag.text.strip().replace('\n',''))
        else:
            zagolovok.append('-')
    print(zagolovok)
    with open('Res.txt','w', encoding="utf-8") as file:
        for el in zagolovok:
            file.write(str(el))
            file.write('\n')