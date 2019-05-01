"""
Web crawler ch01
1. get page from url (urllib類別庫: urlopen)
2. parse tag (bs4類別庫: BeautifulSoup)
BeautifulSoup 需有 argument 用哪種 parser
  - html.parser
  - lxml
"""

from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

url = "http://pythonscraping.com/pages/page1.html"

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        soup = BeautifulSoup(html.read(), 'html.parser')
        title = soup.h1
    except AttributeError as e:
        return None
    return title

title = getTitle(url)
if title == None:
    print("title could not found")
else:
    print(title)