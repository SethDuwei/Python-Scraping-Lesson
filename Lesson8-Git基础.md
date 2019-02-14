### 面向对象

最核心内容

#### 先定义类
对象、属性、方法

##### 定义默认属性__init__

```
class Cat: #建议驼峰
  def __init__(self, name): #特殊方法，用于初始化对象属性
  # 注意 init两边是2个下划线 __ 不是1个 _
    self.name = name
    
tom = Cat("tom") #属性赋值
print(tom.name) #显示 tom
```
如果定义默认属性，创建对象时不赋值，会报错
```
