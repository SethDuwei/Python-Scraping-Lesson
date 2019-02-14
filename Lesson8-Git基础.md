### Git 命令行操作
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

#### 先定义类

##### 定义默认属性__init__

```
class Cat: #建议驼峰
  def __init__(self, name): #特殊方法，用于初始化对象属性
  # 注意 init两边是2个下划线 __ 不是1个 _
    self.name = name
    
tom = Cat("tom") #属性赋值
print(tom.name) #显示 tom
```
