from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import yaml



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

# load data
with open('A:\Projects\Personal-Finance-Tools\sankey\complex_sankey_data.yaml') as f:
    data = yaml.safe_load(f)

# # override gray link colors with 'source' colors
# opacity = 0.4
# # change 'magenta' to its 'rgba' value to add opacity
# data['data'][0]['node']['color'] = ['rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
# data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
#                                     for src in data['data'][0]['link']['source']]

# fig = go.Figure(data=[go.Sankey(
#     valueformat = data['data'][0]['valueformat'],
#     valuesuffix = data['data'][0]['valuesuffix'],
#     # Define nodes
#     node = dict(
#       pad = 15,
#       thickness = 15,
#       line = dict(color = "black", width = 0.5),
#       label =  data['data'][0]['node']['label'],
#       color =  data['data'][0]['node']['color']
#     ),
#     # Add links
#     link = dict(
#       source =  data['data'][0]['link']['source'],
#       target =  data['data'][0]['link']['target'],
#       value =  data['data'][0]['link']['value'],
#       label =  data['data'][0]['link']['label'],
#       color =  data['data'][0]['link']['color']
# ))])

# fig.update_layout(title_text = data['layout']['title']['text'],
#                   font_size = data['layout']['font']['size'],
#                   width = data['layout']['width'],
#                   height = data['layout']['height'])
# fig.show()


#######################################################################################


# override gray link colors with 'source' colors
opacity = 0.4
# change 'magenta' to its 'rgba' value to add opacity
data['data'][0]['node']['color'] = ['rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
                                    for src in data['data'][0]['link']['source']]

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
fig.show()

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(['LA', 'NYC', 'MTL', 'Orschel'],
        'LA',
        id='dropdown'
    ),
    html.Div(id='display-value'),
    dcc.Graph(
        id='graph1',
        figure=fig
        )
])

@app.callback(Output('display-value', 'children'),
                [Input('dropdown', 'value')])
def display_value(value):
    return f'You have selected {value}'


if __name__ == '__main__':
    app.run_server(debug=True)