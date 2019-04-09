import os
import re
import pymysql
from urllib.request import urlopen, urlretrieve
import urllib
from bs4 import BeautifulSoup

# 联系成功，成功将WIKI存入MYSQL数据库中！！！恭喜！！！

'''
s = "2018年中国足球超级联赛"
s = urllib.parse.quote(s)
url = "https://zh.wikipedia.org/wiki/%s" % (s)
# print(url)
'''
url = "https://en.wikipedia.org/wiki/Premier_League"

# 连接数据库
conn = pymysql.connect(host="127.0.0.1", unix_socket="/tmp/mysql.sock",
                       user="root", passwd=None, db="mysql", charset="utf8")
cur = conn.cursor()
cur.execute("USE scraping")

html = urlopen(url)
soup = BeautifulSoup(html, "lxml")
# print(html)
all_titles = soup.find_all("h3")
# 在所有的H3标题中，找到2018-19赛季信息
# 找到该赛季所对应的数据表
for title in all_titles:
    if title.get_text() == "2018–19 season":
        print("现在要输出的信息是："+title.get_text()+"的信息。")
        data_table = title.findNext("table")

# 插入函数很重要，使用转义占位字符代替要插入的变量


def store(num1, num2, num3, num4, num5, num6, num7, num8, num9):
    cur.execute("INSERT INTO premier(club, position, first_in_top, first_in_pre, seasons_in_top, seasons_in_pre, first_season, top_titles,last_top_title) VALUES(\"% s\", \"% s\", \"% s\", \"% s\",\"% s\", \"% s\", \"% s\", \"% s\", \"% s\")",
                (num1, num2, num3, num4, num5, num6, num7, num8, num9))
    cur.connection.commit()


all_data_item = []  # 找一个列表把数据装起来
# 显示出了全部数据，每行一个列表项
for data_row in data_table.find_all("tr"):
    # 从每一列中选择每一个数据项
    # 搜索2个标签，把标签放入字典中
    for data_item in data_row.find_all({"th", "td"}):
        # print(data_item)
        # 把每一个数据项存入列表中
        all_data_item.append(data_item.get_text().replace(
            "\n", "").replace("/a", ""))
    # 每行的数据存入一次
    store(all_data_item[0],  all_data_item[1], all_data_item[2], all_data_item[3],
          all_data_item[4], all_data_item[5], all_data_item[6], all_data_item[7], all_data_item[8])

    '''
    for i in range(8):
        print(all_data_item[i])
    '''
    # print(all_data_item[0])
    all_data_item = []
print("===============================================")
# print(all_data_item)
print("===============================================")

# cur.execute("SELECT * FROM pages")
# print(cur.fetchall())

cur.close()
conn.close()
