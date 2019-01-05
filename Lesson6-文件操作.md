### 文件操作

主要功能：打开、读、写、关闭

#### 打开 open()
```
f = open('test.txt','r')
```
第二个参数为打开方式
* r 只读
* w 写+覆盖
* a 续后面写
* r+ +w
* w+ +r
* a+ +r
```
import os

os.path.abspath('.')
f = open('test.txt','w')
f.write("haha")
f2 = open('test.txt','r')
f2.read() #将内容读取出来，全部内容为一个字符串
f2.readline() # 每次读一行
f2.readlines() #将内容读取出来，每一行作为一个列表元素。
# 每一行用 \n 换行
f2.close()
```
