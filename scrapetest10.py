import os
import re
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

# 要解析的地址，以花瓣网为例
# 打开该地址
html = urlopen("https://huaban.com/boards/51074008/")
# 煲汤
soup = BeautifulSoup(html, "lxml")
# 找到所有的缩略图指向的原图地址
pins = soup.find_all("a", {"class": "img x layer-view"})

number = 1  # 下载重命名计数器
download_dir = "download/"

# 如果下载目录不存在，则新建一个
if not os.path.exists(download_dir):
    os.mkdir(download_dir)

for pins_location in pins:
    # print(pics_location.find("img")["src"])
    # 获得链接到原图的地址
    pin_location_src = "https://huaban.com"+pins_location["href"]
    # print(pin_location_src)
    # 再把每个pin的页面煲汤

    soup1 = BeautifulSoup(urlopen(pin_location_src), "lxml")
    # 找到具体pin页面的原图地址
    pic_location = soup1.find(
        "div", {"class": "image-holder"}).find("img")["src"]
    final_pic_location = "https:"+pic_location
    print(final_pic_location)
    # 下载
    urlretrieve(final_pic_location, download_dir+str(number)+".jpg")
    number = number + 1
