from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from alpha_vantage.timeseries import TimeSeries
from flaskext.mysql import MySQL
import database

app = Flask(__name__)
db = database.Database(app, MySQL())

rows = db.execute("SELECT net_cash FROM BALANCE WHERE user_ID = 0")[0]
print(rows)

# H2AKUMZSFASPIHZH
api = TimeSeries(key='H2AKUMZSFASPIHZH')
# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Portfolio page login required
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/quote', methods=["GET", "POST"])
def quote():
    if request.method == "GET":
        return render_template('quote.html')
    
    elif request.method == "POST":
        data = request.form.get('quote-input')
        try:
            quote = api.get_quote_endpoint(symbol=data)
            print(quote[0]["05. price"])
            data = {'price': float(quote[0]["05. price"]), 'symbol': data}
            return render_template('quote_response.html', data=data)

        except:
            print("failed")
        
        return redirect('/quote')

# Buy page login required
@app.route("/buy", methods=["GET", "POST"])
def buy():
    if request.method == "GET":
        return render_template('buy.html')
    
    elif request.method == "POST":
        data = request.form.get('buy-input')
        quantity = 1
        try:
            stock_price = float(api.get_quote_endpoint(symbol=data)[0]["05. price"]) * quantity

        except:
            print("failed")
            return redirect('/buy')
        
        # Checks if user has enough money to buy the amount of stocks
        user_cash = db.execute("SELECT net_cash FROM BALANCE WHERE user_ID = 0")[0]
        if (user_cash > stock_price):
            # Update the db if the user has enough and update the amount of stocks and subtract the money
            return redirect('/buy')
        
        # If don't user doesn't have enough money tell the user they don't have enough money
        else:
            return redirect('/buy')

# Sell page login requried
@app.route("/sell", methods=["GET", "POST"])
def sell():
    if request.method == "GET":
        # Get all unique stock own by the user and let them choose which one to sell
        return render_template('sell.html')
    
    if request.method == "POST":
        # Subtract amount of stock and add the sold stock's price to the user's net total
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