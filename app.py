from dash import Dash, dcc, html, Input, Output, State
import plotly.graph_objects as go
import yaml
import urllib.request

app = Dash(__name__)
server = app.server

# get data 
url = 'https://raw.githubusercontent.com/Vinnie117/personal-finance-tools/main/sankey/complex_sankey_data.yaml'
response = urllib.request.urlopen(url)
data = yaml.safe_load(response.read())

# Built Sankey with plotly
fig = go.Figure(data=[go.Sankey(
    valueformat = data['data'][0]['valueformat'],
    valuesuffix = data['data'][0]['valuesuffix'],
    # Define nodes
    node = dict(
      pad = 15,
      thickness = 15,
      line = dict(color = "black", width = 0.5),
      label =  data['data'][0]['node']['label'],
      color =  data['data'][0]['node']['color']
    ),
    # Add links
    link = dict(
      source =  data['data'][0]['link']['source'],
      target =  data['data'][0]['link']['target'],
      value =  data['data'][0]['link']['value'],
      label =  data['data'][0]['link']['label'],
      color =  data['data'][0]['link']['color']
))])

fig.update_layout(title_text = data['layout']['title']['text'], # ABC Test
                  font_size = data['layout']['font']['size'],
                  width = data['layout']['width'],
                  height = data['layout']['height'])


# Create web app with dash
app.layout = html.Div(children=[
    html.H1(children='Hello World'),
    html.Div(children='''
        Dashboard: Dies ist eine Testanwendung.
    '''),

    # Sankey Plot
    dcc.Graph(
        id='sankey_graph',
        figure=fig
    ),

    # Textbox for Sankey input
    dcc.Textarea(
    id='sankey',
    value='Gehalt [100] Miete \nGehalt [70] Konsum\nGehalt [30] Sparen',    
    placeholder='Enter a value...',
    style={'width': '100%'}
    ),

    # Test Button -> Button to submit info from Textarea to Sankey
    html.Button('Submit', id='button_1')
])

@app.callback(
    # Output(component_id='output-container-button', component_property='children'),
    # [Input(component_id='button_1', component_property='n_clicks')],
    # [State('input-box', 'value')])
    Output(component_id='sankey_graph', component_property='figure'),
    [Input(component_id='sankey', component_property='value')],
    [State('sankey', 'value')])
def update_sankey(text):
    return 'The input value was "{}" and the button has been clicked {} times'.format(text)

# def updated_sankey() needs to be in callback!


# klären
# -> wie genau erhält die Funktion ihre Argumente im Callback?
# -> wie / wo werden Funktionsinputs erzeugt?




if __name__ == '__main__':
    app.run_server(debug=True)

