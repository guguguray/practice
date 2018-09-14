"""
requests & BeautifulSoup
爬取 ptt 多頁的 網頁連結&標題

"""
import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/beauty/index.html'
number_of_pages = 3

# loop for grep multiple pages
for index in range(number_of_pages):
    print("網頁: " + url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    tag_name = 'div.title a'
    headlines = soup.select(tag_name)

    # 輸出文章標題
    for headline in headlines:
        print(headline)

    # 定義 "上頁" 的標題 tag 並取得前頁的網頁名稱
    tag_page = 'div.btn-group-paging a'
    prev_page = soup.select(tag_page)
    print(prev_page[1])
    prev_url = 'https://www.ptt.cc' + prev_page[1]['href']

    # 網址換成前頁網址
    url = prev_url