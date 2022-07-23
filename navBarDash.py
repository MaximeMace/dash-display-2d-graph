import dash
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd

# Load CSV file with pandas
source = pd.read_csv('fifa_soccer_players.csv')

# Get Data average from CSV pandas
avg_age = soccer['age'].mean()
avg_height = soccer['height_cm']
avg_weight = soccer['weight_kg'].mean()

# Create cards components
cards = dbc.CardDeck([
    dbc.Card(
        dbc.CardBody([
            html.H4('Avg. Age'),
            html.H5(f'{round(avg_age,1)} years')
        ]),
        style={'textAlign': 'center', 'color': 'white'},
        color='lightblue'
    ),
    dbc.Card(
        dbc.CardBody([
            html.H4('Avg. Height'),
            html.H5(f'{round(avg_height,1)} cm')
        ]),
        style={'textAlign': 'center', 'color': 'white'},
        color='blue'
    ),
    dbc.Card(
        dbc.CardBody([
            html.H4('Avg. Weight'),
            html.H5(f'{round(avg_weight,1)} weight')
        ]),
        style={'textAlign': 'center', 'color': 'white'},
        color='darkblue'
    ),
]),

# Create navbar component
navbar = dbc.NavbarSimple(
    brand = 'soccer player dashboard',
    children = [
        html.Img(src='https://favpng.com/png_view/open-case-records-management-case-management-logo-data-management-png/85nV9gwK', height=20),
        html.A('Data source', href="#", target="_blank", style={'color':'black'})
    ],
    color='primary',
    fluid=True
)

# Create dash dashboard with bootstrap
app = dash.Dash(external_stylesheets=dbc.themes.BOOTSTRAP)

# Create layout for dashboard dash
app.layout = html.Div([navbar, html.Br(), cards])




## Check if main program
if __name__=='__main__':
    ## Run dashboard with debug
    app.run_server(debug=True)