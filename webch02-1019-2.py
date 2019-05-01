"""
Web crawler ch02
Advanced BeautifulSoup:
- 走訪樹狀清單
  **子代     .children
  **子代子孫  .descendants
  **處理平輩  .next_siblings
  **處理親代  parent.previous_sibling
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://pythonscraping.com/pages/page3.html"

html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')

namelist = soup.find("table", {"id":"giftList"})
print("=========(.children 子代)=========")
for child in namelist.children:
    print(child)

print("=========(.descendants 子代與子孫)=========")
for child in namelist.descendants:
    print(child)

print("=========(.next_siblings 平輩)=========")
for sibling in namelist.tr.next_siblings:
    print(sibling)


namelist2 = soup.find("img", {"src": "../img/gifts/img1.jpg"})
print("=========(.previous_sibling)=========")
# for sibling in namelist2.parent.previous_siblings:
#     print(sibling)
print(namelist2.parent.previous_sibling)
