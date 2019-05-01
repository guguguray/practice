"""
Grep acticle for multiple pages from ptt site
https://www.ptt.cc/bbs/Beauty/index.html

1. 取得 <上頁 的 url for repeat multiple pages
2. 取得網頁url及標題
3. 建立資料夾
4. 進入個別標題, 建立子資料夾並擷取圖檔 存到本地端
***本地端檔名以標題命名
***標題需要過濾 特殊符號

"""

import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
import os


# 標題過濾符號空格: 避免建立路徑時出現問題
def regen_title(phrase):
    regen_title = ""
    for char in phrase:
        if char in " /?:":      # 比對單字是否含有特殊符號
            regen_title = regen_title + ""
        else:
            regen_title = regen_title + char
    return regen_title

base_url = 'https://www.ptt.cc'
url = 'https://www.ptt.cc/bbs/Beauty/index.html'
reg_imgur_file = re.compile('http[s]?://i.imgur.com/\w+\.(?:jpg|png|gif)')

#setup no of pages to retrive
pages = 1

if not os.path.isdir('images'):
    print("Create Dir:images ...")
    os.mkdir('images')
else:
    print("Dir:images existed...")

for i in range(pages):
    res = requests.get(url)
    # print(res.text)

    soup = BeautifulSoup(res.text, 'lxml')

    #取得上頁的連結
    grep_url = soup.select('div.btn-group.btn-group-paging a')[1]['href']
    prev_url = base_url + grep_url
    print(prev_url)

    # select 取得目前頁面所有連結及標題
    articles = soup.select('div.title a')
    # find_all取得目前頁面所有連結及標題
    # articles = soup.find_all(['div','a'], class_='title')
    #print(articles)

    # 取得每篇文章的標題和連結
    for article in articles:
        #print(article)
        # 呼叫 regen_title 重新過濾各文章標題
        article_title = regen_title(article.text)

        article_url = base_url + article['href']   # 各文章連結 搭配 soup.select() 的取得方法
        #article_url = base_url + article.a['href']  # 各文章連結 搭配 soup.find_all() 的取得方法
        print(article_title, article_url)

        res = requests.get(article_url)
        #print(res.text)
        img_files = reg_imgur_file.findall(res.text)
        #print(img_files)

        #建立 images 下的子資料夾
        if not os.path.isdir(os.path.join('images', article_title)):
            print("Create Sub directory....")
            os.mkdir(os.path.join('images', article_title))
        else:
            print("Sub directory existed...")

        for img in set(img_files):
            print(img)
            # 找出所有檔名, 將其訂為資料夾名稱
            filename = img.split('/')[3]
            print(filename)
            # download img to local
            urlretrieve(img, os.path.join('images', article_title, filename))

        print()

    # repeat loop for prev page
    url = prev_url

