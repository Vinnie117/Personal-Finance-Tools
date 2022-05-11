from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import yaml

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

from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import json, urllib

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Supply chain of the energy production'),
    dcc.Graph(id="graph"),
    html.P("Opacity"),
    dcc.Slider(id='slider', min=0, max=1, 
               value=0.5, step=0.1)
])

@app.callback(
    Output("graph", "figure"), 
    Input("slider", "value"))
def display_sankey(opacity):
    url = 'https://raw.githubusercontent.com/Vinnie117/personal-finance-tools/main/sankey/complex_sankey_data.yaml'
    response = urllib.request.urlopen(url)
    data = yaml.safe_load(response.read())

    node = data['data'][0]['node']
    node['color'] = [
        f'rgba(255,0,255,{opacity})' 
        if c == "magenta" else c.replace('0.8', str(opacity)) 
        for c in node['color']]

    link = data['data'][0]['link']
    link['color'] = [
        node['color'][src] for src in link['source']]

    fig = go.Figure(go.Sankey(link=link, node=node))
    fig.update_layout(font_size=10)
    return fig

app.run_server(debug=True)


