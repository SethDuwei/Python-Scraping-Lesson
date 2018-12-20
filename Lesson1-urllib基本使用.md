## Python 爬虫学习之路 Day1
## urllib request爬取百度首页内容
学习资料：[传智播客python就业班第7阶段课程](https://www.youtube.com/watch?v=Z33ZoslTRTQ&list=PLC664nq_h8b81Eh0jERXmtKk_CWntvUnB&index=6)

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
[urllib.request官方文档](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)
class urllib.request.***Request***(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
This class is an abstraction of a URL request.
创建Request对象实例，以使用更多参数
***需要再回头学习 Python OOP 面向对象编程***

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

#### 3.增加header报头信息，模拟浏览器，避免反爬

***Request***对象中，关于headers参数的定义
> ***headers*** should be a dictionary, and will be treated as if add_header() was called with each key and value as arguments. This is often used to “spoof” the User-Agent header value, which is used by a browser to identify itself – some HTTP servers only allow requests coming from common browsers as opposed to scripts. For example, Mozilla Firefox may identify itself as "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11", while urllib’s default user agent string is "Python-urllib/2.6" (on Python 2.6).

```
#导入urllib模块
import urllib.request

#创建Header头信息，模拟浏览器
user_agent = {"User-Agent":"User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

#创建Request对象的实例，可以使用其他参数，如data,header等
#传递headers参数，模拟浏览器避免被反爬
request = urllib.request.Request("http://www.baidu.com",headers = user_agent)
#urlopen返回一个对象，类似context manager有方法
response = urlopen(request)
#读取打开的对象
html = response.read()

#显示读取的对象
print (html)
```
####结论
以上3种方法都可成功下载并读取百度首页的html文件。
1. 第一段方法回被发爬虫机制屏蔽；
2. 第二段方法实例化Request对象，使用headers参数，模拟浏览器，以达到欺骗发爬虫工具的目的；
3. 第三段代码具体实现headers。
