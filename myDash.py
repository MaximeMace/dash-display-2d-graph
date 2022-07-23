from dash import Dash, html, dcc
import pandas as pd
from dash.dependencies import Input, Output

# Load csv file with pandas
datas = pd.read_csv('salaries.csv')

## Instantiate Dash
app = Dash(__name__)

## Layout Dashboard Dash
app.layout = html.Div([
    html.Div([
        html.H1('Salaries', style={'font-weight': 'bold', 'font-family': 'Montserrat', 'opacity':'0.7'}),
    ]),

    html.Div([
        html.Div([
            html.Label(['Select data in X axis :'], style={'font-weight': 'bold', 'font-family': 'Montserrat', 'opacity':'0.5'}),
            dcc.Dropdown(id="x_axis", 
                options=[{'label':value, 'value':value} for value in datas],
                value=datas.columns[0],
                style={'font-weight': '300', 'font-family': 'Montserrat', 'margin-top': '10px'}
            )
        ], style={'width': '20%', 'display': 'inline-block', 'margin-left':'10px', 'vertical-align':'top'}),

        html.Div([
            html.Label(['Select data in Y axis :'], style={'font-weight': 'bold', 'font-family': 'Montserrat', 'opacity':'0.5'}),
            dcc.Dropdown(id="y_axis", 
                options=[{'label':value, 'value':value} for value in datas],
                value=datas.columns[1],
                style={'font-weight': '300', 'font-family': 'Montserrat', 'margin-top': '10px'}
            ),
        ], style={'width': '20%', 'display': 'inline-block', 'margin-left':'50px', 'vertical-align':'top'}),

        html.Div([
            html.Label(['Do you want line on your graph ?'], style={'font-weight': '600', 'font-family': 'Montserrat', 'opacity':'0.5'}),
            dcc.Checklist(
                id="line_choice", 
                options= [{'label': 'Line', 'value': True}],
                style={'font-weight': '300', 'font-family': 'Montserrat', 'margin-top': '10px'}
            ),
        ], style={'width': '20%', 'display': 'inline-block', 'margin-left':'50px', 'vertical-align':'top'}),
    ], style={ 'background-color': 'white', 'border': '1px solid #F9F9F9', 'padding': '10px', 'margin': '1rem 0rem', 'box-shadow': '0px 0px 30px rgba(0, 0, 0, 0.1)'}),

    html.Div([
        dcc.Graph(id='data_graph', style={'border': '4px solid #F9F9F9'})
     ]),
])

@app.callback(
    Output('data_graph', 'figure'),

    [Input('x_axis', 'value'),
     Input('y_axis', 'value'),
     Input('line_choice', 'value'),],
)

def update_graph(x_axis, y_axis, line_choice):
    return {
        'data': [dict(
            x = datas[x_axis],
            y = datas[y_axis],

            mode = 'lines+markers' if(line_choice is not None and line_choice) else 'markers',

            marker = {
                'size': 15,
                'opacity': 0.5,
                'color': 'red'
            }
        )],

        'layout': dict(
            xaxis = {
                'title': x_axis,
                'type': 'linear'
            },
            yaxis = {
                'title': y_axis,
                'type': 'linear'
            },

            margin = {'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode = 'closest'
        )
    }

## Check if main program
if __name__=='__main__':
    ## Run dashboard with debug
    app.run_server()