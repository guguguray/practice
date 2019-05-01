"""
Web crawler ch03
wikipedia

"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/Kevin_Bacon"

html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

links = soup.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
for link in links:
    # print(link.attrs)
    if "href" in link.attrs:
        print(link.attrs['href'])