# used for graphing 
import plotly.graph_objects as go
from plotly.offline import plot
# used to get data and configure to usable format
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
# used for calculating dates
import datetime
from dateutil.relativedelta import relativedelta
# used to take graph and make it a div string for html
from flask import Markup

def get_stocksyb():
    return stock_symbol

def get_x_axis_dates(id, number):
    date_list = []
    i = 0
    if id = 'day':
        end_date = datetime.datetime.today() + relativedelta(days = -number)
        date_index = datetime.datetime.today()
        date_list.append(date_index)
        if number == 1:
            while date_index.strftime('%Y-%m-%d') != end_date.strftime('%Y-%m-%d'):
                i += 1
                date = datetime.datetime.today() + relativedelta(days = -i)
                date_list.append(date.strftime('%Y-%m-%d'))
                date_index = date
        if number == 5:
            while date_index.strftime('%Y-%m-%d') != end_date.strftime('%Y-%m-%d'):
                i += 1
                date = datetime.datetime.today() + relativedelta(days = -i)
                date_list.append(date.strftime('%Y-%m-%d'))
                date_index = date
        return date_list
    if id = 'month':
        # get the end date to stop and return date_list
        end_date = datetime.datetime.today() + relativedelta(months = -number)
        # get starting date for indexing 
        date_index = datetime.datetime.today()
        # append start date to date_list
        date_list.append(date_index)
        if number == 1:
            # untill date_index get to end_date keep getting every day into date_list
            while date_index.strftime('%Y-%m-%d') != end_date.strftime('%Y-%m-%d'):
                i += 1
                date = datetime.datetime.today() + relativedelta(days = -i)
                date_list.append(date.strftime('%Y-%m-%d'))
                date_index = date
        if number == 6:
            while date_index.strftime('%Y-%m-%d') != end_date.strftime('%Y-%m-%d'):
                i += 1
                date = datetime.datetime.today() + relativedelta(days = -i)
                date_list.append(date.strftime('%Y-%m-%d'))
                date_index = date
        return date_list
    if id = 'year':
        # get the end date to stop and return date_list
        end_date = datetime.datetime.today() + relativedelta(years = -number)
        # get starting date for indexing 
        date_index = datetime.datetime.today()
        # append start date to date_list
        date_list.append(date_index)
        if number == 1:
            # untill date_index get to end_date keep getting every day into date_list
            while date_index.strftime('%Y-%m-%d') != end_date.strftime('%Y-%m-%d'):
                i += 1
                date = datetime.datetime.today() + relativedelta(days = -i)
                date_list.append(date.strftime('%Y-%m-%d'))
                date_index = date
        if number == 5:
            while date_index.strftime('%Y-%m-%d') != end_date.strftime('%Y-%m-%d'):
                i += 1
                date = datetime.datetime.today() + relativedelta(days = -i)
                date_list.append(date.strftime('%Y-%m-%d'))
                date_index = date
        return date_list
    

def get_y_axis_data(id, number):   # id will tell us if its days,months, years
                                    # and number will tell us how many days,months,..
    ts = TimeSeries(key = 'H2AKUMZSFASPIHZH', output_format = 'pandas')
    data = ts.get_daily_adjusted(symbol = stock_symbol, outputsize = 'full')[0]

    # get a all data from a given start date only
    if id = 'day':
        start_date = datetime.datetime.today() + relativedelta(days = -number) 
        clean_data = data[start_date:]['4. close']
        #print(clean_data)
        return clean_data
    if id = 'month':
        start_date = datetime.datetime.today() + relativedelta(months = -number) 
        clean_data = data[start_date:]['4. close']
        #print(clean_data)
        return clean_data
    if id = 'year':
        start_date = datetime.datetime.today() + relativedelta(years = -number) 
        clean_data = data[start_date:]['4. close']
        #print(clean_data)
        return clean_data

def get_stockcharts(stock_symbol, api_key = 'H2AKUMZSFASPIHZH', id, number):
    # get all stock data
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=get_many_dates_month(id, number),
        y=get_cleaned_data(id, number)
    ))

    fig.update_layout(
        margin = dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="LightSteelBlue",
        autosize=True,
        width=650,
        height=550, 
    )

    graph_to_div = Markup(plot(fig, output_type='div'))

    return graph_to_div

    # if id = 'day':
    #     if number = 1:
        
    #     if number = 5:

    # if id = 'month':
    #     if number = 1:

    #     if number = 6:
    # if id = 'year':
    #     if number = 1:

    #     if number = 5: