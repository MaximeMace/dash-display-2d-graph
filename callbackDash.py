from gc import callbacks
import dash 
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input-text', value='Change this text', type='text'),
    html.Div(id='output-text')
])

@app.callback(
    Output(component_id='output-text', component_property='children'),
    Input(component_id='input-text', component_property='value')
)

def updateOutputDiv(input_text):
    return f'Text: {input_text}'


## Check if main program
if __name__=='__main__':
    ## Run dashboard with debug
    app.run_server(debug=True)