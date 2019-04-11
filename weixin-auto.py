'''
程序功能：
1.监测“合美嘉”公众号最新发布文章
2.自动复制文章内容到“简书”账号并发布

开发记录：
1. 20190410
    1-a 打开mac上的微信程序
    1-b 找到微信客户端的搜索框
    1-c 在搜索框中输入要查找的公众号名称
    1-d 一路点击进入公众号“显示历史消息”面板
    1-e “历史消息”面板翻页，刚好显示最新5条文章
    1-f 按数量依次点击文章链接，获取发布日期和文章永久链接
    1-g 调用浏览器显示一遍所有文章，获取文章标题
    1-h 把日期、标题、链接存入CSV本地文件中

难点：
locateOnScreen原函数查找图片非常难，安装opencv-python后，使用confidence=0.9容错率后完美解决。
如果刚开始找不到，用循环反复查找，10次内找到
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui
import time
import os
import pyperclip
import csv

# 图片search匹配模块，原生的不好用，必须加容错机制


def pic_find(pic_name):
    search_found = pyautogui.locateOnScreen(
        pic_name, confidence=0.9)  # 查找图片名称，带后缀
    if search_found == None:  # 如果没找到
        print("找不到图片啊，继续找……")
        search_times = 0

        while search_found is None:
            search_found = pyautogui.locateOnScreen(
                pic_name, confidence=0.8)
            print("又没找到，再等1秒再找……")
            search_times += 1
            time.sleep(1)
            if search_times > 30:
                break
            # 如果找了30次还没找到直接跳出
        print("终于找到啦！图片的地址如下：")
        print(search_found)
    search_position = pyautogui.center(search_found)  # 找到匹配图片的中心点坐标
    return search_position  # 返回找到图片的坐标


# 自动打开微信程序


def weixin_open():
    os.system("open /Applications/wechat.app")  # 打开微信
    time.sleep(2)  # 等待时间非常重要，等app加载出来
    print("请稍等5秒钟，等微信出来了……")
    # locateOnScreen找到图片的概率太低，仅一个纯绿色图片找到匹配
    login_found = pyautogui.locateOnScreen(
        'weixin-login.png')  # 先找微信的登录按钮
    if login_found == None:  # 如果没找到登录按钮
        print("难道你已经登录了？我检查一下！")
        # 没找到登录按钮，可能已登录成功，直接调用“查找”功能
    else:  # 如果已经找到登录按钮
        login_button_position = pyautogui.center(login_found)
        # 把四位坐标变为X,Y两位坐标

        print("找到登录按钮啦，坐标是："+str(login_button_position.x) +
              ","+str(login_button_position.y))  # 显示登录按钮的中心坐标
        pyautogui.click(login_button_position.x, login_button_position.y)
        print("微信已打开，请在手机上确认登录")


# 找到公众号搜索框并点击
def weixin_find_search():
    time.sleep(2)  # 等待微信界面显示
    print("请稍等5秒钟，等微信界面刷新出来了……")
    search_position = pic_find("weixin-search.png")
    pyautogui.click(search_position.x, search_position.y)


# 输入要搜索的公众号名称
def weixin_search(weixin_name):
    #foo = u'合美嘉国际教育'
    pyperclip.copy(weixin_name)
    time.sleep(2)
    pyautogui.hotkey('command', 'v')  # Mac系统得用Command+V复制
    time.sleep(1)
    # pyautogui.press('enter')
    # time.sleep(1)
    # pyautogui.typewriter不能输入中文，只能用pyperclip复制粘贴

# 打开“查看历史消息”界面


def weixin_show():
    # 搜索到公众号后，一路点开直到“查看历史消息”
    # 仅根据mac air的分辨率进行定位，容错率很低
    pyautogui.move(yOffset=80)
    pyautogui.click()
    time.sleep(1)
    pyautogui.move(xOffset=660, yOffset=-80)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.move(xOffset=-50, yOffset=260)
    time.sleep(1)
    pyautogui.click()


# 打开“历史消息”后，滚屏后刚好显示5篇文章
def weixin_check_update():
    time.sleep(2)
    if_loaded = pic_find("hp-logo-small.png")
    if if_loaded != None:
        print("公众号历史界面加载成功！")
        # 界面加载成功后再找最新一篇文章
        position = pic_find("faxiaoxi.png")  # 找到“发消息”按钮
        time.sleep(1)
        pyautogui.moveTo(position.x, position.y)  # 鼠标移到“发消息“按钮下
        pyautogui.scroll(-4)  # 向下滚动鼠标
# 自动监测公众号更新


# 采集最上面文章的发布日期
def weixin_display_date():

    time.sleep(2)
    # pyautogui.move(yOffset=-16)  # 放到文章标题上
    # time.sleep(1)
    pyautogui.move(xOffset=-260, yOffset=30)  # 移动到日期“日”字右边
    pyautogui.mouseDown()  # 按下鼠标左键
    time.sleep(1)
    pyautogui.dragRel(xOffset=-100, duration=1)  # 向左边拖动鼠标
    # pyautogui.move(xOffset=-100)  # 移动到日期“2”字左边
    pyautogui.hotkey('command', 'c')
    time.sleep(1)
    # pyautogui.mouseUp()  # 放开鼠标左键
    article_date = pyperclip.paste()
    print("文章发表的日期是："+article_date)
    # 再返回文章标题位置
    time.sleep(1)
    pyautogui.move(xOffset=360, yOffset=-30)
    return article_date
    # return lastest_articles_dates  # 返回整个日期列表

# 复制最新文章的链接后返回历史列表
# 可输入采集文章的数量
# 返回所有文章链接的列表
# 采集链接的同时，采集发布日期


def weixin_copy_link(article_number):
    lastest_articles = []  # 最新文章列表链接
    lastest_articles_dates = []  # 最新文章发布时间
    time.sleep(2)
    pyautogui.move(yOffset=-16)  # 放到文章标题上
    for i in range(article_number):
        article_date = weixin_display_date()  # 采集文章发布日期
        lastest_articles_dates.append(article_date)  # 把文章日期添加到列表中
        time.sleep(2)
        default_position = pyautogui.position()  # 先存储现在鼠标坐标
        print("当前的坐标是：")
        print(default_position)
        pyautogui.click()  # 当前默认位置先点击
        time.sleep(3)
        if pic_find("hp-article-title.png") != None:  # 先找到具体文章显示后的“合美嘉”文字
            print("第"+str(i+1)+"篇文章已经成功加载啦！")
            link_position = pic_find("copy-link.png")  # 找到“复制链接”按钮
            pyautogui.click(link_position.x, link_position.y)  # 复制该链接到剪切板
            new_link = pyperclip.paste()  # 复制该链接到变量
            lastest_articles.append(new_link)  # 所有链接放到列表中
            print("采集到第"+str(i+1)+"篇文章啦！链接是：")
            print(new_link)  # 打印链接
        time.sleep(2)
        pyautogui.press("backspace")  # 返回原来链接
        time.sleep(3)
        pyautogui.moveTo(default_position.x,
                         default_position.y+104+i)  # 挪到下一篇文章
    print("这次一共采集了"+str(len(lastest_articles))+"篇文章，好累呀！我的工作都在下面啦：")
    for links in lastest_articles:  # 挨个显示链接
        print(links)
    return lastest_articles, lastest_articles_dates  # 将采集文章链接的列表返回

# 在浏览器中显示所有链接 | 测试功能
# 返回所有文章标题


def weixin_display_title(all_links):
    lastest_articles_titles = []  # 存储所有文章标题
    print("本次采集的文章标题是：")
    for link in all_links:
        browser = webdriver.Chrome()
        browser.get(link)
        element = browser.find_element_by_xpath("//h2")
        lastest_articles_titles.append(element.text)
    for title in lastest_articles_titles:  # 打印文章标题
        print(title)
        # print(link)
    return lastest_articles_titles

    '''
    for i in range(article_number):
        time.sleep(2)
        default_position = pyautogui.position()  # 先存储现在鼠标坐标
        print("当前的坐标是：")
        print(default_position)
        pyautogui.click()  # 当前默认位置先点击
    '''
# 采集这一堆文章的发布日期

# 将采集的文章信息写入CSV文件


def store_csv(date, title, link):
    headers = ['date', 'title', 'link']
    with open('weixin_auto.csv', 'a+') as f:
        f_csv = csv.writer(f)
        rows = []
        # 每个元组作为列表元素
        for i in range(len(date)):  # 插入列表
            item = ()  # 创建一个元组
            item = (date[i], title[i], link[i])  # 按每个元素顺序放入元组
            rows.append(item)  # 将该元组存入列表
            del item  # 删除元组，重新新建一个元组再存入列表
        print(rows)

        f_csv.writerow(headers)  # 写入表头
        f_csv.writerows(rows)  # 写入数据
        print("数据都已成功存入CSV文件中啦！")
# 将采集的文章信息写入CSV文件


def read_csv():
    with open('weixin_auto.csv', newline='') as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            i += 1
            if i == 2:
                # print(row[0])
                lastest_date = row[0]
    return lastest_date  # 返回最新一篇文章的日期
# 打印出来数据文件


def weixin_copy():
    pass
# 单个文章复制功能


def jianshu_login():
    pass
# 简书登录模块


def jianshu_publish():
    pass
# 简书发布模块


def jianshu_report():
    pass
# 简书发布报告


weixin_open()  # 打开微信
time.sleep(2)
weixin_find_search()  # 检查公众号历史文章
time.sleep(1)
weixin_search("合美嘉国际教育")  # 在搜索框查找公众号名称
weixin_show()  # 显示“查看历史消息”面板
weixin_check_update()  # 在“历史消息”面板翻屏，刚好显示5篇文章
article_list = weixin_copy_link(5)  # 采集几篇文章,同时调用采集日期函数
article_titles = weixin_display_title(article_list[0])  # 显示所有文章标题列表,输入值为所有链接

dates = article_list[1]  # 日期列表 article_list[1]
titles = article_titles  # 标题列表 article_titles
links = article_list[0]  # 链接列表 article_list[0]
print(dates, titles, links)
#store_csv(dates, titles, links)
new_date = read_csv()  # 已经存储的最新的文章日期
print("已经更新过的最新文件日期是："+new_date)
if new_date == dates[0]:
    print("已经是最新的文章啦，不用更新！")
else:
    store_csv(dates, titles, links)  # 将日期、标题、链接存入CSV文件中
