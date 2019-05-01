"""
grep info from google search
param : 'q': 關鍵字

"""
import requests
from bs4 import BeautifulSoup

myparam = {'q': '寒流'}
url = 'https://www.google.com.tw/search'

res = requests.get(url, params = myparam)
#print(res.status_code)
print(requests.codes.ok)

if res.status_code == requests.codes.ok:
    soup = BeautifulSoup(res.text, 'html.parser')
    #print(soup.prettify())

    items = soup.select('div.g > h3.r > a[href^="/url"]')
    for item in items:
        print(item['href'], item.text)