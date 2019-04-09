from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = "http://pythonscraping.com/pages/page3.html"
html_content = urlopen(html)
# print(html_content.read())
soup = BeautifulSoup(html_content, "lxml")
for gift_list in soup.find_all("tr", {"class": "gift"}):
    print(gift_list.find(
        "img", {"src": re.compile("\.\.\/img\/gifts\/img.\.jpg")}))
