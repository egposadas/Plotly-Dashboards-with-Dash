#######
# This provides examples of Dash Core Components.
# Feel free to add things to it that you find useful.
######
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(
    children=[
        dcc.Dropdown(
            options=[
                {'label': 'new York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='MTL',
        ),
        
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value=['MTL', 'SF'],
            multi=True
        ),
        
        # SLIDER https://dash.plot.ly/dash-core-components/slider
        html.Label('Slider'),
        html.P(
            dcc.Slider(
                min=-10,
                max=10,
                step=0.5,
                marks={i: i for i in range(-10,11)},
                value=0
            )
        ),
        # RADIO ITEMS https://dash.plot.ly/dash-core-components/radioitems
        html.Label('Radio Items'),
        dcc.RadioItems(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='MTL'
        )
    ],
    style = {'width':'50%'}
    
)

if __name__ == '__main__':
    app.run_server()
    