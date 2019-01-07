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
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-30-620f82777a8d> in <module>
     12         #print("大家好我是",self.name)
     13 
---> 14 tom = Cat()
     15 tom.name

TypeError: __init__() missing 1 required positional argument: 'name'
```

私有属性
```__self.name = name ```
私有方法
```def __test(self):```

##### 定义__str__方法
作用：在使用 print(tom) 的时候设置默认打印输出项。如不使用，print出为tom对象地址

```<__main__.Cat object at 0x7fb6df53abe0>```

如定义__str___方法，则修改print(对象)后的输出，如：

```
  def __str__(self):
    return "hello,我是默认打印方法" # 注意，该方法必须return
```

print(tom)输出为“hello，我是默认打印方法”


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
