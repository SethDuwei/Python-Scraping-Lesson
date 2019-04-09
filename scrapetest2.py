from urllib.request import urlopen
from bs4 import BeautifulSoup
print('###########################################')
html = urlopen("http://pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, "html.parser")
find_gift = soup.find_all('tr', {'class': 'gift'})
# gift_name = find_gift.find('td')
find_gift.contents
