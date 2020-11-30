import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.dmzj.com/view/yaoshenji/41917.html'
r = requests.get(url=url)
html = BeautifulSoup(r.text, 'lxml')
script_info = html.script
pics = re.findall(r'\d{13,14}', str(script_info))
for idx, pic in enumerate(pics):
    if len(pic) == 13:
        pics[idx] = pic + '0'
pics = sorted(pics, key=lambda x: int(x))
after = re.findall(r'\|\|(\d{5})', str(script_info))[0]
front = re.findall(r'\|jpg\|(\d{4})', str(script_info))[0]
for pic in pics:
    if pic[-1] == '0':
        url = 'https://images.dmzj.com/img/chapterpic/' + front + '/' + after + '/' + pic[:-1] + '.jpg'
    else:
        url = 'https://images.dmzj.com/img/chapterpic/' + front + '/' + after + '/' + pic + '.jpg'
    print(url)