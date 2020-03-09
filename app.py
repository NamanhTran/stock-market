from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from alpha_vantage.timeseries import TimeSeries
import MySQLdb
import database

app = Flask(__name__)
db = MySQLdb.connect(host="localhost",
                        user = "root",
                        passwd = "Namanhtran1!",
                        db = "STOCK_TRADER")
cur = db.cursor()

cur.execute("SELECT net_cash FROM BALANCE WHERE user_ID = 0")
rows = cur.fetchone()
print(float(rows[0]))
db.commit()

user_id = 0
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
        symbol = request.form.get('buy-input')
        quantity = 1

        try:
            stock_price = float(api.get_quote_endpoint(symbol=symbol)[0]["05. price"]) * quantity

        except:
            print("failed")
            return redirect('/buy')
        
        # Checks if user has enough money to buy the amount of stocks
        cur = db.cursor()
        cur.execute("SELECT net_cash FROM BALANCE WHERE user_ID = 0")
        user_cash = cur.fetchone()[0]
        if (user_cash > stock_price):
            # Update the db if the user has enough and update the amount of stocks and subtract the money
            user_cash = user_cash - stock_price
            cur.execute("UPDATE BALANCE SET net_cash = %d WHERE user_ID = %s" % (user_cash, user_id))
            
            cur.execute("SELECT stock_ID FROM STOCK WHERE stock_ID = '%s' AND user_ID = %s" % (symbol, user_id))
            exist = cur.fetchone()
            if exist:
                cur.execute("SELECT quantity, market_value FROM STOCK WHERE stock_ID = '%s' AND user_ID = %s" % (symbol, user_id))
                data = cur.fetchone()
                updated_quantity = int(data[0]) + quantity
                updated_market_value = float(data[1]) + stock_price
                cur.execute("UPDATE STOCK SET quantity = %s, market_value = %s WHERE stock_ID = '%s' AND user_ID = %s" % (updated_quantity, updated_market_value, symbol, user_id))
            
            else:
                cur.execute("INSERT INTO STOCK (user_ID, stock_ID, quantity, market_value) VALUES (%s, '%s', %s, %s)" % (user_id, symbol, quantity, stock_price))

            db.commit()
            cur.close()
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
        symbol = request.form.get('sell-input')
        quantity = 1
        try:
            stock_price = float(api.get_quote_endpoint(symbol=symbol)[0]["05. price"]) * quantity
            print(stock_price)

        except:
            print("failed")
            return redirect('/sell')

        cur = db.cursor()
        cur.execute("SELECT quantity FROM STOCK WHERE stock_ID = '%s' AND user_ID = %s" % (symbol, user_id))
        user_quantity = cur.fetchone()[0]

        if user_quantity >= quantity:
            cur.execute("SELECT net_cash FROM BALANCE WHERE user_ID = 0")
            updated_cash = float(cur.fetchone()[0]) + stock_price
            print(updated_cash)
            cur.execute("UPDATE BALANCE SET net_cash = %d WHERE user_ID = %s" % (updated_cash, user_id))

            updated_quantity = user_quantity - quantity
            cur.execute("UPDATE STOCK SET quantity = %s WHERE stock_ID = '%s' AND user_ID = %s" % (updated_quantity, symbol, user_id))
        
        db.commit()
        cur.close()

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