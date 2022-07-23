## Basic import
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output, States

## Load csv file with pandas
data = pd.read_csv('world_happiness.csv')

regionOptions = [{'label': i, 'value':i} for i in data['region'].unique()]
# countryOptions = [{'label': i, 'value':i} for i in data['country'].unique()]
# lineFig = px.line(data[data['country'] == 'United States'], x='year', y='happiness_score', title='Happiness in USA')
dataOptions = [{'label': 'data score', 'value': 'data_score'},{'label': 'data rank', 'value': 'data_rank'}]

## Instantiate Dash
app = dash.Dash()

## Section all the time define in dash file
app.layout = html.Div([
    html.H1('Expectancy all around the world'),
    html.P(['The Dashboard shows the expectancy on world']),
    html.A('Source data reference', href='', target='_blank'),
    dcc.RadioItems(id='region-radio', options=regionOptions, value='North America'),
    dcc.RadioItems(options= regionOptions, value='North America'),
    dcc.Checklist(options= regionOptions, value=['North America']),
    dcc.Dropdown(id="country-dropdown"),
    dcc.RadioItems(id='data-radio', options=dataOptions, value='data_score'),
    html.Br(),
    html.Button(id="submit-button", n_clicks= 0, children="Update the button"),
    dcc.Graph(id='data-graph'),
    html.Div(id='average-div')
])

@app.callback(
    Output('country-dropdown', 'options'),
    Output('country-dropdown', 'value'),
    Input('region-radio', 'value'),
)

def updateDropdown(selectedRegion):
    filtered_data = data[data['region'] == selectedRegion]
    countryOptions = [{'label':i, 'value':i} for i in filtered_data['country'].unique()]
    return countryOptions, countryOptions[0]['value']

@app.callback(
    Output('data-graph', 'figure'),
    Output('average-div', 'children'),
    Input('submit-button-state', 'n_clicks'),
    State("country-dropdown", 'value'),
    State('data-radio', 'value')
)

def update_graph(buttonClick, selectedCountry, selectedData):
    filtered_data = data[data['country'] == selectedCountry]
    lineFig =  px.line(filtered_data, x='year', y='happiness_score', title=f'{selectedData} in {selectedCountry}')

    selectedAverage = filtered_data[selectedData].mean()
    return lineFig, f'The average data {selectedData} for {selectedCountry} is {selectedAverage}'

## Check if main program
if __name__=='__main__':
    ## Run dashboard with debug
    app.run_server(debug=True)