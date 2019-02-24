### Flask基本命令
安装、运行基本命令
```
pip3 install flask
```

最简单的flask文件
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return ("Hello,world!!!!")
```

在flask中运行python文件
```
export FLASK_ENV=development
FLASK_APP=hello.py flask run
打开调试模式，每次修改py文件自动启动服务器实现
不然得手动重启服务器
```

直接展示一个html文件，在template目录下
```
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
```

py后台文件在html文件中插入参数
```
py文件如下
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    headline = "Hello, world!"
    return render_template("index.html", headline=headline)
```
```
在html文件内插入参数{{headline}}
{{}}这是jinja2的语法，flask使用
<!DOCTYPE html>
<html>
<head>
    <title>
        INDEX PAGE
    </title>
</head>

<body>
    <h1>{{ headline }}</h1>
</body>
</html>
```

使用flask就必须用到jinja?
表达式：条件判断的用法，在html文件中
```
{% if True %}
```
