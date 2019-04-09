import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://news.163.com/")
soup = BeautifulSoup(html, "lxml")
image = soup.find("img", {"alt": "求求你们，放过武大的樱花吧"})

directory = "download"  # 下载目录
if not os.path.exists(directory):
    os.mkdir(directory)
download_directory = "download/2.jpg"

image_link = image['src']
print(image_link)
print(type(image_link))
urlretrieve(image_link, download_directory)
