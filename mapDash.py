import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import dash_table
import plotly.express as px

# Load csv file with pandas
electricity = pd.read_csv('electricity.csv')

# Get min and max year
year_min= electricity['year'].min()
year_max= electricity['year'].max()

app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR])

app.layout = html.Div([
    html.H1('Electricity price'),
    dcc.RangeSlider(id='year-slider',
        min= year_min,
        max= year_max,
        value= [year_min, year_max],
        marks= {i:str(i) for i in range(year_min, year_max + 1)},
    ),
    dcc.Graph(id='map-graph',figure=map_fig),
    dash_table.DataTable(
        id='price-info', 
        columns=[{'name': col, 'id': col} for col in electricity.columns], 
        data=electricity.to_dict('records'))
])

@app.callback(
    Output('price-info', 'data'),
    Input('map-graph','clickData'),
    Input('year-slider', 'value')
)

def update_data_table(clicked_data, selected_years):
    filtered_electricity = electricity[(electricity['Year']>= selectedYear[0]) & (electricity['Year'] <= selectedYear[1])]

    if clicked_data is None:
        return []
    
    us_state = clicked_data['points'][0]['location']
    filtered_electricity = electricity[electricity['US_State'] == us_state]

    return filtered_electricity.to_dict('records')