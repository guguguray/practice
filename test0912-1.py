"""
requests 請求 practice:

.status_code
.encoding

"""
import re
import requests
from bs4 import BeautifulSoup

# Requests practice
url = 'http://blog.castman.net/web-crawler-tutorial/ch1/connect.html'
r = requests.get(url)

print(r.status_code)
print(r.encoding)
print(r.headers)
print()
# print(r.text)
# print(r.content)

"""
BeautifulSoup 解析 practice
.find_all()
.find()
"""

# 原始 HTML 程式碼
html_doc = '<html>' \
           '<head>' \
           '<title>Hello World</title>' \
           '</head>' \
           '<body><h2>Test Header</h2>' \
           '<p>This is a test.</p>' \
           '<a id="link1" href="/my_link1">Link 1</a>' \
           '<a id="link2" href="/my_link2">Link 2</a>' \
           '<p>Hello, <b class="boldtext">Bold Text</b></p>' \
           '</body></html>'

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())   # HTML 結構經過排版後輸出
print(soup.contents)
print(soup.select('html'))

print()
print("[輸出標籤 title] __________________________")
print(soup.title)
print(soup.title.string)   # 加上 .string 可過濾標籤, 直接輸出內容

print()
print("[find_all 標籤 a] __________________________")
tags_a = soup.find_all('a') # 找尋a標籤結果放入 array

print(tags_a)        # 輸出 array 形式
print(tags_a[1])     # 輸出 array 中 index:1 item
for tag in tags_a:   # 輸出 各 item
    print(tag)

print()
print("[find_all 多重標籤 a. title] __________________________")
tags_multi = soup.find_all(['a', 'title'])  # 找尋多種標籤結果放入 array
print(tags_multi)        # 輸出 array 形式
for tag in tags_multi:
    print(tag)

links = soup.find_all(href=re.compile("^/my_link\d"))
print(links)


