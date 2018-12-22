## Python 爬虫学习之路 Day3
### post get模拟爬百度搜索
学习资料：[传智播客python就业班第7阶段课程](https://www.youtube.com/watch?v=s0MwZMSel8k&list=PLC664nq_h8b81Eh0jERXmtKk_CWntvUnB&index=7)
继续反爬虫机制

#### 1.urllib.parse.urlencode()编码使用
Python3中，urlencode()在parse模块中
```from urllib.parse import urlparse```

> urllib.parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus)
> Convert a mapping object or a sequence of two-element tuples, which may contain str or bytes objects, to a percent-encoded ASCII text string. If the resultant string is to be used as a data for POST operation with the urlopen() function, then it should be encoded to bytes, otherwise it would result in a TypeError.

#### 2.基础不牢，倍受打击
在本课程中，使用urlopen(full_url)方式，full_url = url（前缀）+ wd（解码后的关键词）
已经可成功用GET方式发出请求

但，在百度贴吧爬虫程序设计课程中，碰到了namespace、OOP设计、文件操作等基础问题
此方面内容几乎没有学习，导致学习停滞
现在返回头认真学习基础课程
传播智客的内容还是相当不错的

#### 3.Linux基本操作
[【python基础】之linux教学 day1-08-命令的基本格式、ls选项 黑马程序员/传智播客](https://www.youtube.com/watch?v=LKk_Rtjyh2A&index=8&list=PLNTlJhYDV6sNBSVrIiA_QfIQwk4sPVsBj)
根据此内容从最基本的开始练习，打好扎实基础

连接远程CentOS服务器
ssh root@**.**.**.*** -p 26128
退出 logout

```
TAB 自动补全文件名
ls --help 显示帮助文件
man ls mannual文件
ls -a # 显示全部文件
ls -l # 显示详细文件信息
ls -l -h # 增加显示文件大小
ls -lah

# 参数先后顺序不影响效果
cd
clear
```

