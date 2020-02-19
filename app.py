from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/buy", methods=["GET", "POST"])
def buy():
    if request.method == "GET":
        return render_template('buy.html')

@app.route("/sell", methods=["GET", "POST"])
def sell():
    if request.method == "GET":
        return render_template('sell.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')