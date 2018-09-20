"""
Grep images from html page
"""

import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve


url = 'https://www.ptt.cc/bbs/beauty/index.html'
reg_imgur_file = re.compile('http[s]?://i.imgur.com/\w+\.(?:jpg|png|gif)')

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

tag_name = 'div.title a'
articles = soup.select(tag_name)

for article in articles:
    each_url = 'https://www.ptt.cc' + article['href']
    print(each_url + article.text)
    res2 = requests.get(each_url)
    images = reg_imgur_file.findall(res2.text)
    print(images)
    print()
    # 擷取圖檔的亂碼檔名，(用set方式避開重複檔名)
    for image in set(images):
        ID = re.search('http[s]?://i.imgur.com/(\w+\.(?:jpg|png|gif))',image).group(1)
        print(ID)
        urlretrieve(image,ID)




