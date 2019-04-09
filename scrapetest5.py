from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
soup = BeautifulSoup(html, "lxml")
print(soup.find("div", "id": "bodyContent"))
# for link in soup.find("div",{"id":"bodyContent"})
