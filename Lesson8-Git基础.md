### Git 命令行操作
熟悉以下基本操作，即可满足日常git工作需求。
还缺分支branch使用与合并命令

复制远程库到本地
```
git clone https:\\
```
添加文件到暂存区
```
git add file.name
```
确认将更新的文件添加到库
```
git commit -m "message" file.name
```
显示当前编辑库的状态
```
git status
```
把更新库内容推送到线上库
```
git push
```
把线上库内容取回来
有人在之前更新了线上库，push会出问题
先用pull同步内容，再push即可
```
git pull
```
显示所有的命令历史
```
git log
```
重置命令
根据log命令出的hash码
返回之前的某一版本
```
git reset --hard hashcode
```
