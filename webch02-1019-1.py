"""
Web crawler ch02
Advanced BeautifulSoup:
- soup.findAll(tagName, tagAttribute)
- ex:
    soup.findAll("span", {"class":"green"})

- 取得不含標籤, 只有文字: name.get_text()
- find() & findAll() 有何不同
  findAll(tag, attributes, recursive, text, limit, keywords)
  find(tag, attributes, recursive, text, keywords)

  **取得物件清單 >> 用 findAll
  **取得單一物件 >> 用 find
  **使用 keywords 搜尋時, 如果是用 (class="green") >> 會發生錯誤
    必須改用 (class_="green")
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://pythonscraping.com/pages/warandpeace.html"

html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')

namelist = soup.findAll("span", {"class":"green"}, text = "the prince")
for name in namelist:
    print(name)            # 包含標籤及內容文字
    #print(name.get_text())  # 只取內容文字，不含標籤

print("=========================================")
namelist2 = soup.find("span", {"class":"green"})
for name in namelist2:
    print(name)            # 包含標籤及內容文字
    #print(name.get_text())  # 只取內容文字，不含標籤