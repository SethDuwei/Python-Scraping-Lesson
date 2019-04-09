from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

html = urlopen("http://www.pythonscraping.com")
soup = BeautifulSoup(html, "lxml")
all_item = soup.find_all(src=True)
os.mkdir("download")
for file in all_item:
    # print(file)

    print(file["src"])
    urlretrieve(file, "download")
# 巨大的问题：一定要注意学习
# find_all输出为list[]
# for item in list:后输出为带标签列表
# <script src="http://www.pythonscraping.com/misc/jquery.js?v=1.4.4" type="text/javascript"></script>
# 用item["src"]可输出具体标签内容
# http://www.pythonscraping.com/misc/jquery.js?v=1.4.4
# 为什么？难道list[]中的单个元素为字典？？？？
# 暂时没有找到答案
