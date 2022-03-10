import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

# ---Creating DATA
np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

# ---Scatterplot 1
data1 = [go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',
    marker = {
        'size':12,
        'color': 'rgb(51,204,153)',
        'symbol':'pentagon',
        'line':{'width':2}
    }
)]
layout1 = go.Layout(
    title='First Plot',
    xaxis = {'title':'Some X 1 title'}
)

# ---Scatterplot 2
data2 = [go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',
    marker = {
        'size':12,
        'color': 'rgb(200,204,53)',
        'symbol':'pentagon',
        'line':{'width':2}
    }
)]
layout2 = go.Layout(
    title='Second Plot',
    xaxis = {'title':'Some X 2 title'}
)

app.layout = html.Div([
    dcc.Graph(
        id='scatterplot1',
        figure = {'data':data1, 'layout':layout1}
    ),
    dcc.Graph(
        id='scatterplot2',
        figure = {'data':data2, 'layout':layout2}
    )
])

if __name__ == '__main__':
    app.run_server()
