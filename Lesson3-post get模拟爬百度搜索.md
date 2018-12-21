## Python 爬虫学习之路 Day3
### post get模拟爬百度搜索
学习资料：[传智播客python就业班第7阶段课程](https://www.youtube.com/watch?v=s0MwZMSel8k&list=PLC664nq_h8b81Eh0jERXmtKk_CWntvUnB&index=7)
继续反爬虫机制

#### 1.urllib.parse.urlencode()编码使用
Python3中，urlencode()在parse模块中
```from urllib.parse import urlparse```

> urllib.parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus)
> Convert a mapping object or a sequence of two-element tuples, which may contain str or bytes objects, to a percent-encoded ASCII text string. If the resultant string is to be used as a data for POST operation with the urlopen() function, then it should be encoded to bytes, otherwise it would result in a TypeError.


