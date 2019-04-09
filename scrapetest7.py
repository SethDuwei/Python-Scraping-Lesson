from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup
import re
import random
import webbrowser


def get_links(url_address):
    # 读输入网址数据
    html = urlopen("https://en.wikipedia.org"+url_address)  # 先读取http数据
    soup = BeautifulSoup(html, "lxml")  # 再用soup解析
    # 读出所有在div bodyContent下的href=/wiki/*的所有a标签
    # 先找div，然后找div下所有满足正则表达式的a tag
    # find_all()输出的是列表
    all_a = soup.find("div", {"id": "bodyContent"}).find_all(
        "a", {"href": re.compile("\/wiki\/*")})
    print("在这个页面中一共获取了"+str(len(all_a))+"个词条链接。")
    random_a = random.randint(0, len(all_a)-1)  # 随机获取一个链接
    print("现在显示的是第"+str(random_a)+"个链接。")
    return all_a[random_a].attrs['href']  # 显示该链接
    # 遍历a列表，一个一个显示出来
    # attrs输出的是字典
    '''
    for link in all_a:
        if 'href' in link.attrs:
            return(link.attrs['href'])  # 显示具体的链接
    '''


# 从其中获取一个随机链接
new_address = get_links("/wiki/Lionel_Messi")
# 显示第一个随机链接
print(new_address)
print("===================================================")
print("第二个页面的链接是:")
# 获得第二个随机链接
new_address_2 = get_links(new_address)
# 显示第二个随机链接
print(new_address_2)
# 打开在第二个页面找到的随机链接
webbrowser.open_new_tab("https://en.wikipedia.org"+new_address_2)
