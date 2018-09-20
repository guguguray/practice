"""
try to grep asoboo site's
- ps4 product name
- price

Beautifulsoup 解析查找方式有兩種:
1. .select()
    用 CSS 選擇器的語法, 通過tag標籤逐行查找:
    如:
        soup.select("body a")    #body子標籤中的a標籤
        soup.select(".class名稱") #尋找某個特定class
        soup.select("#id名稱")    #尋找某個特定id
        soup.select("p > a:nth-of-type(2)") #找到某個tag標籤下的第二個子標籤

2. .find_all()
    搜索目前tag的所有tag子節點,並判断是否符合過濾器的條件
    如:
        css_soup.find_all("p", class_="body")
        # [<p class="body strikeout"></p>]


"""

import requests
from bs4 import BeautifulSoup

source = "http://asoboo.ddns.net/joomla/index.php/tw/%E9%9B%BB%E7%8E%A9%E5%A8%9B%E6%A8%82/tv%E9%81%8A%E6%88%B2/ps4"

res = requests.get(source)
# print(res.text)

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.prettify())

"""
.select 的方式透過tag標籤逐行找
好處是遇到多重標籤如: 
<div class="product vm-col span3">
<div class="product vm-col span3 virticle">

***使用 .select 方式上面兩行都會搜尋出來
soup.select(".product.vm-col.span3")
***用 .find_all 只會找到第一行
soup.find_all("div", class_="product vm-col span3") 
""""

# 使用 select 方式:
#products = soup.select(".product.vm-col.span3")
#print(products)

#for product in products:
#    title = product.select('div h2')[0].text
#    price = product.select(".PricesalesPrice")[1].text
#    print(title, price)

# 使用 find or find_all 方式
products = soup.find_all("div", class_="product vm-col span3")
print(products)



