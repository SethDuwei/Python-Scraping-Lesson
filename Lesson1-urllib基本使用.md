## urllib基本使用
## urllib request爬取百度首页内容

'''
#导入urllib模块
import urllib.request

#百度网址
url = "http://www.baidu.com"
#urlopen返回一个对象，类似context manager有方法
response = urlopen(url)
#读取打开的对象
html = response.read()

#显示读取的对象
print (html)
'''
