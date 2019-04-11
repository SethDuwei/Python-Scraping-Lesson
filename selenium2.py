# 读取网易新闻当天“要闻“标题
# 使用selenium选取元素，pyautogui协助显示JS内容

from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui
import time

url = "https://news.163.com/"
#html = urlopen(url)
#soup = BeautifulSoup(html, "lxml")
browser = webdriver.Chrome()
browser.get(url)
element = browser.find_element_by_link_text("要闻")
# 打开网页后等待加载，然后滚动到底部，再等待第2页加载
'''
time.sleep(10)
pyautogui.press('pagedown', presses=50, interval=1)
time.sleep(10)
'''
# print(element.text)
# 完美打印出所有首次加载的新闻标题
# 网易新闻需要第一次滚动到底，JS再自动刷新新标题
# 可以使用pyautogui模拟键盘动作手动处理滚动到底
# 然后再每次点击“+加载更多”手动刷新新闻列表，直到全部正常显示

# 获取所有“要闻”的a链接
all_titles = browser.find_elements_by_xpath('//div[@class="news_title"]/h3/a')
# 显示标题数量
news_numbers = len(all_titles)
print("今天的要闻共有：" + str(news_numbers) + "篇。谢谢")
# 打印出所有标题
for news_title in all_titles:
    print(news_title.text)
