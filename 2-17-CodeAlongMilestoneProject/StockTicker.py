#######
# First Milestone Project: Develop a Stock Ticker
# dashboard that either allows the user to enter
# a ticker symbol into an input box, or to select
# item(s) from a dropdown list, and uses pandas_datareader
# to look up and display stock data on a graph.
######

# EXPAND STOCK SYMBOL INPUT TO PERMIT MULTIPLE STOCK SELECTION
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import pandas_datareader.data as web # requires v0.6.0 or later
from datetime import datetime


app = dash.Dash()

# Retrie the information from NASDAQcompanylist.csv
nsdq = pd.read_csv('../data/NASDAQcompanylist.csv')
nsdq.set_index('Symbol', inplace=True)
options = [{'label':'{} {}'.format(tic,nsdq.loc[tic]['Name']), 'value':tic} for tic in nsdq.index]

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),

    html.Div([
        html.H3('Select a stock:'),
        dcc.Dropdown(id='stock_picker', 
            options=options,
            value=['TSLA'],
            multi=True
        )
    ], style = {'width':'45%','display':'inline-block','verticalAlign':'top'}),

    html.Div([
        html.H3('Select range date:'),
        dcc.DatePickerRange(id='date_picker',
            min_date_allowed=datetime(2015, 1, 1),
            max_date_allowed=datetime.today(),
            start_date=datetime(2018, 1, 1),
            end_date=datetime.today()
        )
    ], style = {'width':'45%','display':'inline-block'}),

    html.Div([
        html.Button(id='submit-button',
            n_clicks=0,
            children='Submit'             
        ),
    ], style = {'width':'10%','display':'inline-block'}),

    dcc.Graph(id='stock')
    
])

@app.callback(
    Output('stock', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [   State('stock_picker', 'value'),
        State('date_picker', 'start_date'),
        State('date_picker', 'end_date')        
    ]
)
def update_stock(n_clicks, stock_picker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    traces = []

    for x in stock_picker:
        df = web.DataReader(x,'iex',start,end)
        traces.append({'x':df.index, 'y': df.close, 'name':x})
    
    fig = {
        'data': traces,
        'layout': {'title':', '.join(stock_picker)+' Closing Prices'}
    }
    return fig

if __name__ == '__main__':
    app.run_server()