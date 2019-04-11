'''
程序功能：
1.监测“合美嘉”公众号最新发布文章
2.自动复制文章内容到“简书”账号并发布

开发记录：
1. 20190410
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui
import time
import os


def pic_find(pic_name):
    search_found = pyautogui.locateOnScreen(
        pic_name, confidence=0.9)  # 查找图片名称，带后缀
    if search_found == None:  # 如果没找到
        print("找不到图片啊，继续找……")
        search_times = 0
        while search_found is None:
            search_found = pyautogui.locateOnScreen(
                pic_name, confidence=0.9)
            print("又没找到，再等1秒再找……")
            search_times += 1
            time.sleep(1)
            if search_times > 30:
                break
            # 如果找了30次还没找到直接跳出

        print("终于找到啦！搜索框的地址如下：")
        print(search_found)
    search_position = pyautogui.center(search_found)  # 找到匹配图片的中心点坐标
    return search_position

# 打开公众号历史文章列表


def weixin_history():
    position = pic_find("hp-article-title.png")
    pyautogui.click(position.x, position.y)


# 检查公众号历史文章
weixin_history()
