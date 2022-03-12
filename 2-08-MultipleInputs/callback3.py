#######
# Here we'll use the mpg.csv dataset to demonstrate
# how multiple inputs can affect the same graph.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('../data/mpg.csv')
df['brand'] = df['name'].str.split(' ').str[0]

features = df.columns

app.layout = html.Div(
    children = [
        html.Div(
            children = [
                dcc.Dropdown(id='xaxis',
                    options=[{'label': i, 'value': i} for i in features],
                    value='displacement',
                )
            ],
            style={'width': '48%', 'display': 'inline-block'}   
        ),
        html.Div(
            children = [
                dcc.Dropdown(id='yaxis',
                    options=[{'label': i, 'value': i} for i in features],
                    value='acceleration',
                )
            ],
            style={'width': '48%', 'float': 'right', 'display': 'inline-block'}
        ),
        dcc.Graph(id='feature-graphic')
    ],
    style={'padding':10}
)

@app.callback(
    Output('feature-graphic', 'figure'),
    [   Input('xaxis', 'value'),
        Input('yaxis', 'value')
    ]
)
def update_graph(xaxis_name, yaxis_name):
    traces=[]
    for i in df.brand.unique():
        df_by_brand = df[df['brand']==i]
        traces.append(go.Scatter(
            x=df_by_brand[xaxis_name],
            y=df_by_brand[yaxis_name],
            text=df_by_brand['name'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'title': xaxis_name.title()},
            yaxis={'title': yaxis_name.title()},
            # margin={'l': 10, 'b': 10, 't': 10, 'r': 10},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server()