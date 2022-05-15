from dash import Dash, dcc, html, Input, Output, State
import plotly.graph_objects as go
import yaml
import urllib.request
from sankey import test

app = Dash(__name__)
server = app.server

# get data 
# url = 'https://raw.githubusercontent.com/Vinnie117/personal-finance-tools/main/sankey/complex_sankey_data.yaml'
# response = urllib.request.urlopen(url)
# data = yaml.safe_load(response.read())

# data for local testing
with open('A:\Projects\Personal-Finance-Tools\sankey\complex_sankey_data.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Built Default Sankey with plotly
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

fig.update_layout(title_text = data['layout']['title']['text'], 
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
    value='Gehalt [100] Budget \nDividenden [20] Budget \n\nBudget [70] Miete \nBudget [30] Konsum \nBudget [20] Sparen',    
    style={'width': '100%', 'height': 200}
    ),

    # Test Button -> Button to submit info from Textarea to Sankey
    html.Button('Submit', id='button_1', n_clicks=0)
])

@app.callback(
    Output(component_id='sankey_graph', component_property='figure'),
    [Input(component_id='button_1', component_property='n_clicks')],
    [State('sankey', 'value')])
def update_sankey(dummy_n_clicks, text):

    fig2 = go.Figure(data=[go.Sankey(
    valueformat = data['data'][0]['valueformat'],
    valuesuffix = data['data'][0]['valuesuffix'],
    # Define nodes
    node = dict(
      pad = 15,
      thickness = 15,
      line = dict(color = "black", width = 0.5),
      #label =  [text.split()[1], "Miete", "Konsum", "Sparen"]
      label =  test.nodes(text)[0]
      #label =  data['data'][0]['node']['label']
    ),
    # Add links
    link = dict(
      #source =  data['data'][0]['link']['source'],
      source = test.nodes(text)[1],
      #target =  data['data'][0]['link']['target'],
      target = test.nodes(text)[2],
      value =  test.link_value(text),
      label =  data['data'][0]['link']['label'],
      color =  data['data'][0]['link']['color']
    ))])

    return fig2


if __name__ == '__main__':
    app.run_server(debug=True)




# klären
# -> wie genau erhält die Funktion ihre Argumente im Callback? -> wie / wo werden Funktionsinputs erzeugt?
#    -> return value of Input() and State() will be used for function argument

# -> component_properties sind Funktionsargumente?
'''
Whenever an input property changes, the function that the callback decorator wraps will get 
called automatically. Dash provides this callback function with the new value of the input 
property as its argument, and Dash updates the property of the output component with
whatever was returned by the function.
'''
# - need to connect State() with the button

# - evtl. nur eine einzige Zeile in dem Textfeld durchreichen und ein minimales Sankey im Callback bauen?
# - ein 2. Textfeld im Frontend einbauen um den Text, mit dem das Callback-Sankey gebaut wird zu prüfen
#   - gibt es dafür eine einfachere Lösung? -> einfach in einem neuen Python-skript

# https://dash.plotly.com/basic-callbacks#dash-app-with-state
# https://dash.plotly.com/dash-core-components/textarea
# https://dash.plotly.com/dash-core-components#button
