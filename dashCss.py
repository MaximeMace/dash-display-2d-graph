import dash 
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

soccer = pd.read_csv('fifa_soccer_player.csv')

player_name_options = [{'label': i, 'value': i}  for i in soccer['long_name'].unique()]

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div([
    dbc.Row([
        dbc.Col([ 
            html.H1('Socces player dash'),
            html.P(['Source: ', html.A('Sofifa', href='#', target='_blank')]),
        ]),
       
        dbc.Col([
            html.Label('Player name: '),
            dcc.Dropdown(options= player_name_options, value= player_name_options[0]['value'])
        ])
    ])
], style={'padding': 100, 'border': 'solid'})
