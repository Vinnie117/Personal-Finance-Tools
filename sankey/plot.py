import plotly.graph_objects as go
import yaml

#######################################################
# load data
with open('.\sankey\data.yaml') as f:
    data = yaml.safe_load(f)

# url = 'https://raw.githubusercontent.com/Vinnie117/personal-finance-tools/main/sankey/complex_sankey_data.yaml'
# response = urllib.request.urlopen(url)
# data = yaml.safe_load(response.read())
#######################################################

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
#     color =  data['data'][0]['node']['color'] 
#     x = [0.5],      # manual position of the node! -> can match with annotation in add_annotation()
#     y = [0.8]
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

# # distribute annotation evenly?
# # -> plot is in space between coordinates [0,1] for x and y -> specify annotations relatively
# fig.add_annotation(dict(font=dict(color='black',size=10),
#                                         x=0.9,
#                                         y=0.725,
#                                         showarrow=False,
#                                         text=data['data'][0]['link']['value'][0],
#                                         textangle=0,
#                                         xanchor='left',
#                                         xref="paper",
#                                         yref="paper"))

#fig.show()