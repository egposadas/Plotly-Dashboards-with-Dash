#######
# This uses a small wheels.csv dataset
# to demonstrate multiple outputs.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import base64

app = dash.Dash()

df = pd.read_csv('../data/wheels.csv')

# Get encode image
def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

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
    html.Div(id='colors-out'),

    html.Img(id='display_img', src='children', height='100px')
    
], style={'fontFamily':'helvetica', 'fontSize':18})

# Get the Wheels
@app.callback(
    Output('wheels-out', 'children'),
    [Input('wheels', 'value')]
)
def callback_w(wheels_value):
    return 'You\'ve selected "{}"'.format(wheels_value)

# Get the Colors
@app.callback(
    Output('colors-out', 'children'),
    [Input('colors', 'value')]
)
def callback_c(colors_value):
    return 'You\'ve selected "{}"'.format(colors_value)

# Get the Image
@app.callback(
    Output('display_img', 'src'),
    [Input('wheels', 'value'),
     Input('colors', 'value')])
def callback_img(wheel, color):
    path = '../data/images/'
    return encode_image(path + df[(df['wheels'] == wheel) & (df['color'] == color)]['image'].values[0])
    

if __name__ == '__main__':
    app.run_server()
