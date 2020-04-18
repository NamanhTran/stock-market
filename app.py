from plotlyCharts import *
@app.route('/results', methods=['GET', 'POST'])
def results():
    # change the stock symbol to whatever
    # the string can be either day, month, year
    # the number depends on string type
        # day can be 1, 5
        # month can be 1, 6
        # year can be 1, 5
        # these can also be changed
    return render_template('example.html', div_placeholder=get_stockcharts('MSFT', 'month', 6))