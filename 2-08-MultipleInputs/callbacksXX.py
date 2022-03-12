#######
# This is Dash's tutorial script for multiple inputs
# using Chris Parmer's indicators.csv dataset
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'cb5392c35661370d95f300086accea51/raw/'
    '8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/'
    'indicators.csv')

indicators = df['Indicator Name'].unique()

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(id='xaxis-col',
                options=[{'label':i, 'value':i} for i in indicators],
                value='Fertility rate, total (births per woman)'
            ),
            dcc.RadioItems(id='xaxis-type',
                options=[{'label':i, 'value':i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ], style={'width': '48%', 'display': 'inline-block'}),
        html.Div([
            dcc.Dropdown(id='yaxis-col',
                options=[{'label':i, 'value':i} for i in indicators],
                value='Life expectancy at birth, total (years)'
            ),
            dcc.RadioItems(id='yaxis-type',
                options=[{'label':i, 'value':i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator_grf'),

    dcc.Slider(id='year_slider',
        min=df['Year'].min(),
        max=df['Year'].max(),
        value=df['Year'].max(),
        step=None,
        marks={str(year): str(year) for year in df['Year'].unique()}
    )
    
], style={'padding':10})


@app.callback(
    Output('indicator_grf', 'figure'), 
    [   Input('xaxis-col', 'value'),
        Input('yaxis-col', 'value'),
        Input('xaxis-type', 'value'),
        Input('yaxis-type', 'value'),
        Input('year_slider', 'value')
    ]
)
def update_grf(xaxis_col, yaxis_col, xaxis_type, yaxis_type, year):
    dfy = df[df['Year']==year]
    return {
        'data': [go.Scatter(
            x=dfy[dfy['Indicator Name']==xaxis_col]['Value'],
            y=dfy[dfy['Indicator Name']==yaxis_col]['Value'],
            text=dfy[dfy['Indicator Name']==yaxis_col]['Country Name'],
            mode='markers',
            marker={
                'size': 15,
                'opacity':0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )], 

        'layout': go.Layout(
            xaxis={
                'title': xaxis_col,
                'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_col,
                'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            hovermode='closest'  
        )
        
    }


if __name__ == '__main__':
    app.run_server()