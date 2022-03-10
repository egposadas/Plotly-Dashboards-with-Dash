#######
# This provides examples of Dash HTML Components.
# Feel free to add things to it that you find useful.
######
import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(
    children=[
        'This is the outermost div',
        html.Div(
            'This is an inner Div',
            style={
                'color':'blue',
                'border':'blue',
                'border':'2px blue solid',
                'borderRadius':5,
                'padding':10,
                'width':220
            }
        ),
        html.Div(
            'This is another inner Div',
            style={
                'color':'orange',
                'border':'2px orange solid',
                'borderRadius':5,
                'padding':10,
                'width':220
            }
        )
    ],
    # this styles the outermost Div:
    style={
        'width':250,
        'height':120,
        'color':'red',
        'border':'2px red dotted'
    }
)

if __name__ == '__main__':
    app.run_server()
    
