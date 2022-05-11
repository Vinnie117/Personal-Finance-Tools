from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import yaml
import urllib.request

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = Dash(__name__, external_stylesheets=external_stylesheets)

# server = app.server



# app.layout = html.Div([
#     html.H2('Hello World'),
#     dcc.Dropdown(['LA', 'NYC', 'MTL', 'Orschel'],
#         'LA',
#         id='dropdown'
#     ),
#     html.Div(id='display-value')
# ])

# @app.callback(Output('display-value', 'children'),
#                 [Input('dropdown', 'value')])
# def display_value(value):
#     return f'You have selected {value}'


# if __name__ == '__main__':
#     app.run_server(debug=True)

#################################################################

app = Dash(__name__)
server = app.server

# get data 
url = 'https://raw.githubusercontent.com/Vinnie117/personal-finance-tools/main/sankey/complex_sankey_data.yaml'
response = urllib.request.urlopen(url)
data = yaml.safe_load(response.read())

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

app.layout = html.Div(children=[
    html.H1(children='Hello World'),

    html.Div(children='''
        Dashboard: Dies ist eine Testanwendung.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

