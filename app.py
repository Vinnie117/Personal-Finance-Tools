from dash import Dash, dcc, html, Input, Output, State
import plotly.graph_objects as go
import yaml
import urllib.request
from sankey import functions

app = Dash(__name__)
server = app.server

###############################################################
# get data 
url = 'https://raw.githubusercontent.com/Vinnie117/personal-finance-tools/main/sankey/complex_sankey_data.yaml'
response = urllib.request.urlopen(url)
data = yaml.safe_load(response.read())

# # for local testing
# with open('.\sankey\complex_sankey_data.yaml', 'r') as file:
#     data = yaml.safe_load(file)

##############################################################

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
        figure=fig,
        style={'width': '640px', 'height': '400px'}
    ),

    # Textbox for Sankey input
    dcc.Textarea(
    id='sankey',
    value='Gehalt [100] Budget \nNebeneinkommen [20] Budget \n\nBudget [70] Miete \nBudget [30] Konsum \nBudget [20] Sparen',    
    style={'width': '100%', 'height': 200}
    ),

    # Button to submit info from Textarea to Sankey
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
      label =  functions.nodes(text)[0]
    ),
    # Add links
    link = dict(
      source = functions.nodes(text)[1],
      target = functions.nodes(text)[2],
      value =  functions.link_value(text),
      label =  data['data'][0]['link']['label'],
      color = functions.link_colour(text)
    ))])

    return fig2


if __name__ == '__main__':
    app.run_server(debug=True)
