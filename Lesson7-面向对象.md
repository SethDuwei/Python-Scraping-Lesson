### 面向对象

最核心内容

#### 先定义类
对象、属性、方法

##### 定义默认属性

```
class Cat: #建议驼峰
  def __init__(self, name): #特殊方法，用于初始化对象属性
    self.name = name
    
tom = Cat("tom") #属性赋值
print(tom.name) #显示 tom
```
如果定义默认属性，创建对象时不赋值，会报错
```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-30-620f82777a8d> in <module>
     12         #print("大家好我是",self.name)
     13 
---> 14 tom = Cat()
     15 tom.name

TypeError: __init__() missing 1 required positional argument: 'name'
```

##### 定义方法

```
class Cat: #建议驼峰
  def eat(self): #必须self
    print ("eating...")
```
#### 再创建对象

创建对象
```
tom = Cat()
```
