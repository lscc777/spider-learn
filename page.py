import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = 'https://www.dmzj.com/info/yaoshenji.html'
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    bs = BeautifulSoup(html, 'lxml')
    texts = bs.find('ul', class_='list_con_li autoHeight').find_all('a')
    for text in texts:
        title = text.get('title')
        href = text.get('href')
        print(title)
        print(href)