### 函数知识学习

经过Linux基本操作知识学习，vi基本操作学习，接EDX的Python基础课程（变量、注释、字符串操作、list、tuple、dictionary操作等），继续学习函数相关知识。

```
def wendu()
  wendu = 22
  return wendu
```
> 将重复使用的功能进行封装，是重要的编程思想

定义函数，return后方可将函数赋值给其他变量。且return必须为函数内的变量

return可返回多个值，用list来封装

```return [a,b,c]```

可用tuple来封装

```return (a,b,c)```

#### 四种函数
1. 无参数无返回值
2. 无参数有返回值
3. 有参数无返回值
4. 有参数有返回值

#### 函数默认默认参数

默认值的常用使用方式
```
def test(a,b=0)
  pass
```
  
* 默认参数必须放到参数列的最后

如需要接收多个默认值，可用tuple、dictionary接收
* *args tuple
* **kwargs dictionary

```
def test(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

A = (55,66)
B = {"name":"duwei","age":18}

test(1,11,*A,**B)

输出：
1
11
(55, 66)
{'name': 'duwei', 'age': 18}
```
#### 函数递归调用

函数递归调用有难点，死循环，无法退出。
暂时不解决，留到后期有用到时再学习。

#### 匿名函数
匿名函数默认自带return，适用于非常简单功能的函数
不重要，放下，后续有需要再学习
lambda a,b:a+b
lambda 参数:公式


