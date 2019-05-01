"""
Web crawler ch02
正規表達式: regex
regex 測試網站 http://regexpal.com
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

print("*", " :a*:a這個字至少出現0次或1次以上就符合規則")
print("+", " :a+:a這個字至少出現1次或1次以上就符合規則")
print("[]", " :符合方括號內的任一字元.....就符合規則")
print("()", " :子表達群組, 優先順序處理")
print("{m,n}", " :a{2,3}:符合a字元出現2到3次...就符合規則: 如 aab aaab ")
print("[^]", " :符合任一不在方括號內的字元.就符合規則")
print("|", " :d(i|o)g:dg中間只要是 i或o 字元就符合規則: 如: dig dog")
print(".", " :a.c:ac中間只要是任何字元或符號都符合規則: 如: a&c apc")
print("^", " :^a:符合a開頭的字元或單字......都符合規則: 如: app asdf")
print("\\", "  :跳脫字元 如: (點)\. (豎)\| (斜線)\/ (反斜線)\\\\")
print("$", "  :放在正規式的結尾??????")
print("?!", "  :不包含????????????")

url = "http://pythonscraping.com/pages/page3.html"

html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')

namelist = soup.findAll("img")
for name in namelist:
    print(name)

print("=========(以正規表示法 只找 ../img/gifts/img*.jpg)=========")
print("拆解 \. \. \/ img \/ gifts \/ img.* \.jpg")
formatting = "\.\.\/img\/gifts\/img.*\.jpg"
print("========================================================")

images = soup.findAll("img", {"src": re.compile(formatting)})
for image in images:
    print(image)

print("===尋找擁有兩個屬性的標籤 lambda tag: len(tag.attrs) == 2===")
tests = soup.findAll(lambda tag: len(tag.attrs) == 2)
for test in tests:
    print("---------------------")
    print(test)