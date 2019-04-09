from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
soup = BeautifulSoup(html, "lxml")
# find结果可以find_all
# find_all输出为列表list[]
all_a = soup.find("div", {"id": "bodyContent"}).find_all(
    "a", {"href": re.compile("\/wiki\/*")})
for link in all_a:
    if 'href' in link.attrs:  # attrs的输出是字典，遍历字典提取
        print(link.attrs['href'])
