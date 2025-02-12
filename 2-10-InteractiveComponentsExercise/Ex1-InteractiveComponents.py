#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
app.layout = html.Div([
    dcc.RangeSlider(id='slider',
        min=-10, max=10,
        step=None,
        marks={i: str(i) for i in range(-10, 11)},
        value=[-3, 4]
    ),
    html.H2(id='output')
], style={'width':'50%'})

# Create a Dash callback:
@app.callback(
    Output('output', 'children'),
    [Input('slider', 'value')])
def update_value(value_list):
    return 'The product of the selection is: {}'.format(value_list[0]*value_list[1])

# Add the server clause:
if __name__ == '__main__':
    app.run_server()