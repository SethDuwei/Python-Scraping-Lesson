## Python 爬虫学习之路 Day2
### User-Agent addheader()深度模拟浏览器
学习资料：[传智播客python就业班第7阶段课程](https://www.youtube.com/watch?v=s0MwZMSel8k&list=PLC664nq_h8b81Eh0jERXmtKk_CWntvUnB&index=7)
继续反爬虫机制

#### 1.Random基础使用
Random包是Python自带模块，用于生成随机数

访问[Random官方文档](https://docs.python.org/3/library/random.html)

> This module implements pseudo-random number generators for various distributions.

#### 2.VS Code + Git安装和使用
参考教程[Python Tutorial for Programmers - Python Crash Course](https://www.youtube.com/watch?v=f79MRyMsjrQ&t=2209s)

使用VSCode作为编辑器，并使用Python、Pylint插件构建IDE
VSCode可与[Git整合进行版本管理](https://code.visualstudio.com/docs/introvideos/versioncontrol)，牛！

在MAC上安装Git
学习资料：[廖雪峰的git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013743256916071d599b3aed534aaab22a0db6c4e07fd0000)
[Mac Git安装地址](https://git-scm.com/book/zh/v1/%E8%B5%B7%E6%AD%A5-%E5%AE%89%E8%A3%85-Git)
安装好后
1. 在选定目录中使用 git init 创建 repository
```
git init
$ mkdir Git/Python
$ cd Python
$ pwd
/Users/.../Git/Python
$ git init
Initialized empty Git repository in /Users/.../Git/Python/.git/
```
>所有的版本控制系统，其实只能跟踪文本文件的改动，比如TXT文件，网页，所有的程序代码等等，Git也不例外。
>强烈建议使用标准的UTF-8编码，所有语言使用同一种编码，既没有冲突，又被所有平台所支持。
>***千万不要使用Windows自带的记事本编辑任何文本文件***。原因是Microsoft开发记事本的团队使用了一个非常弱智的行为来保存UTF-8编码的文件，他们自作聪明地在每个文件开头添加了0xefbbbf（十六进制）的字符，你会遇到很多不可思议的问题。

2. 修改文件后，add添加索引
```git add <file>```
注意，可反复多次使用，添加多个文件

3. add后，用commit在repository中确认修改
```git commit -m <message>```

