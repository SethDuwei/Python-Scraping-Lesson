from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    headline = "Hello, Duwei!"
    return render_template("index.html", headline=headline)


@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)


"""
@app.route("/")
def index():
    return ("Hello,world!!!!")
"""

"""
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return (f"<h1>Hello,Your name is {name}!</h1>")
"""
