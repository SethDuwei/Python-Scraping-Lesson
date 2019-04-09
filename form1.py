import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 该程序显示失败，无法显示提交的姓名信息
# 不知道如何解决 ？？？？？？？？？？？？
#params = {'firstname': 'Hi', 'last': 'There'}
r = requests.post(
    'http://pythonscraping.com/files/processing.php', data={'name': '1', 'email': '2'})
#html = urlopen("http://pythonscraping.com/files/processing.php")
#soup = BeautifulSoup(html, "lxml")
# print(soup)
print(r.text)
