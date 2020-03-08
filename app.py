from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from alpha_vantage.timeseries import TimeSeries

app = Flask(__name__)
# H2AKUMZSFASPIHZH
api = TimeSeries(key='H2AKUMZSFASPIHZH')
# Home page
@app.route('/')
def home():
    print(api.get_monthly('GOOGL'))
    return render_template('home.html')

# Portfolio page login required
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

# Buy page login required
@app.route("/buy", methods=["GET", "POST"])
def buy():
    if request.method == "GET":
        return render_template('buy.html')
    
    elif request.method == "POST":
        data = request.form.get('input')
        print(api.get_quote_endpoint(symbol=data))
        return redirect('/buy')

# Sell page login requried
@app.route("/sell", methods=["GET", "POST"])
def sell():
    if request.method == "GET":
        return render_template('sell.html')

# login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')

# register page 
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')