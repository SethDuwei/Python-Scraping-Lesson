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
SSH Secure Shell的缩写
Mac Unix Linux都自带SSH，Windows没有！
```
ssh root@**.**.**.*** -p 26128
退出 logout
```

```
通配符 ? 一个字符串 * 多个字符
TAB 自动补全文件名
ls --help 显示帮助文件
man ls mannual文件
ls -a # 显示全部文件
ls -l # 显示详细文件信息
ls -l -h # 增加显示文件大小
ls -lah
cd 进入目录
cd ~ 进入自己当前账户的home目录

touch 新建文件
rm 删除文件/删除目录
rm -f 不提示直接删除文件
rm -r 递归删除目录和文件
rmdir 删除目录
cat 查看文件

# 参数先后顺序不影响效果
cd
clear
touch 新建文件
cat 查看文件
history 查看历史命令

# 重定向
ls > demo.txt 将命令内容输出到一个文件中（覆盖）
ls >> demo.txt 将新内容重定向到此文件中（末尾追加不覆盖）

more 分屏显示查询内容

# 查找命令
find / -name "*name*" 在指定目录查找名字

# 压缩与解压缩
打包，不压缩
tar -cvf test.tar打包的文件名 *.py 要打包的文件
解包
tar -xvf test.tar 解开
gz压缩
tar -zcvf test.tar.gz *.py
tar -zxvf test.tar.gz 解压缩

# 系统管理相关的命令
cal 日历 cal -y 2018
date 日期
ps process status 查看系统进程
ps -aux 系统当前运行的所有程序
top 显示最消耗资源的进程 q 退出top程序
htop 显示更全的资源使用信息表 # CentOS没有此命令
kill pid 杀死进程

reboot 重启
shutdown -h now 立即关机

```

#### 以下信息为使用vs code进行git管理后添加更新
git使用方法及vs code与github联动在逐步练习中
使用vs code和Github连接进行版本管理，同步到线上使用***如此爽快***！

今天意外使用code写文档，竟然搞明白了git和code联动工作的问题。
1. code以及git插件正常安装；
2. git已连接至Github本人的账号，已通过SSH；
3. 每次修改保存后，git显示change，stage change后再commit
4. commit后再push到Github，至此和网页端同步成功！

**之前的问题**
没有学会基本的git原理和基本使用方式。匆忙开始vs code和git插件的联动，结果卡在save commit push的过程中。在更进一步之前还是要做好基础的学习。图形界面只是简化了命令行工具的使用，没搞清楚命令行的原理，只摸索图形工具也是困难重重。

**系统管理命令**
```
grep 查找内容相关的文本信息 PIP管道使用
df -h disk free 硬盘使用情况
du -h disk usage 当前目录和文件的大小
ifconfig # 查看IP信息,类似windows上的ipconfig命令
ifconfig | grep 97 管道输出文本相关信息，查找含有97的文本段
ping # 网络连通测试命令
```
**用户管理命令**
Linux命令的学习不用面面俱到，简单了解即可，大概知道解决方案，碰到实际问题再查询巩固
多用户登录，证明unix的多用户属性
```
sudo Super User do
su Switch User
useradd new_user -m 添加用户 -m在home目录下创建同用户名目录
passwd new_user 添加密码
userdel 删除用户
groupadd 新建组
groupdel 删除组
groupmod 查看现有所有组名
sudo usermod -a -G sudo 用户名 将用户名加入sudo组中获得sudo权限
su new_user
exit 退出当前账户
```

**文件权限修改命令**
drwxrwxrwx 典型文件权限结构
1：是否目录；
2：拥有者权限 u
3：同组人权限 g
4：其他人权限 o
```
chmod u=rwx file_name 增加rwx权限
r=4 w=2 x=1 # 可用数字法编辑权限
```

