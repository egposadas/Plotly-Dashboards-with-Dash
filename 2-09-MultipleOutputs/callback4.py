#######
# This uses a small wheels.csv dataset
# to demonstrate multiple outputs.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash()

df = pd.read_csv('../data/wheels.csv')
print(df)

app.layout = html.Div([
    dcc.RadioItems(id='wheels',
        options=[{'label':i, 'value':i} for i in df['wheels'].unique()],
        value=1
    ),
    html.Div(id='wheels-out'),

    html.Hr(), # add a horizontal rule

    dcc.RadioItems(id='colors',
        options=[{'label':i, 'value':i} for i in df['color'].unique()],
        value='blue'
    ),
    html.Div(id='colors-out')
], style={'fontFamily':'helvetica', 'fontSize':18})

@app.callback(
    Output('wheels-out', 'children'),
    [Input('wheels', 'value')]
)
def callback_w(wheels_value):
    return 'You\'ve selected "{}"'.format(wheels_value)

@app.callback(
    Output('colors-out', 'children'),
    [Input('colors', 'value')]
)
def callback_c(colors_value):
    return 'You\'ve selected "{}"'.format(colors_value)

if __name__ == '__main__':
    app.run_server()
