"""
requests & BeautifulSoup Lesson
爬取 ptt 單頁的標題及連結

"""

import requests
from bs4 import BeautifulSoup

# 定義網址
url = 'https://www.ptt.cc/bbs/beauty/index.html'

r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')

# 定義要抓取的tag 名稱
tag_name = "div.title a"
headlines = soup.select(tag_name)

# 定義網站的 Domain Name
site = 'https://www.ptt.cc'
for item in headlines:
    print(item)
    print(item['href'])
    # print(site + item['href'], item.text)
