import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/loop")
def loop():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("newyear.html", names=names)
