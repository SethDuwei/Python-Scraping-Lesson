from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, 'lxml')
images = soup.find_all(
    "img", {"src": re.compile("\.\.\/img\/gifts\/img.\.jpg")})
for img in images:
    print(img.attrs['src'])

#print(soup.find("tr", {"id": "gift1"}).children)

# for child in soup.find_all("img"):
#    print(child)

# for child in soup.find("table", {"id": "giftlist"}):
#    print(child)


'''
all_data = soup.find_all('tr', {'class': 'gift'})
for gift_name in all_data:
    # print(gift_name.find('td').string)
    print(gift_name.find('td', string='Vegetable Basket'))
# print(all_data[1])
'''
