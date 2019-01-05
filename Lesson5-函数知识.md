### 函数知识学习

经过Linux基本操作知识学习，vi基本操作学习，接EDX的Python基础课程（变量、注释、字符串操作、list、tuple、dictionary操作等），继续学习函数相关知识。

```
def wendu()
  wendu = 22
  return wendu
```
  
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
```
def test(a,b=0)
  pass
  
默认参数必须放到最后
```

