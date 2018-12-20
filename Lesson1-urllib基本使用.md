## urllib基本使用
## LESSON1 urllib request爬取百度首页内容

#### 1.最简单的读取方法
缺点：没有封装header头，容易被发爬虫

```
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
```

#### 2.创建Request实例
class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
This class is an abstraction of a URL request.
[urllib.request官方文档](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)

```
#导入urllib模块
import urllib.request

#创建Request对象的实例，可以使用其他参数，如data,header等
request = urllib.request.Request("http://www.baidu.com")
#urlopen返回一个对象，类似context manager有方法
response = urlopen(request)
#读取打开的对象
html = response.read()

#显示读取的对象
print (html)
```
