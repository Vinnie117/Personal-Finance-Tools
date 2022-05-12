import plotly.graph_objs as go
import plotly.offline as py
py.init_notebook_mode()
import numpy as np

data = dict(
type='sankey',
node = dict(
  pad = 15,
  thickness = 20,
  line = dict(
    color = "black",
    width = 0.5
  ),
  label = ["A1", "A2", "B1", "B2", "C1", "C2"],

  color = ["blue", "blue", "blue", "blue", 
  "gray", "white"]),#attempt to make it less visible

link = dict(
  source = [0,1,0,2,3,3],
  target = [2,3,3,4,4,5],
  value = [8,4,2,8,4,2],
  # attempt to add labels
  label= [8,4,2,8,4,2]))

layout =  dict(
title = "Basic Sankey Diagram",
font = dict(
  size = 10
 ),
    annotations=[
        dict(
            x=0.25,
            y=0.75,
            text='8',
            showarrow=False
        ),
        dict(
            x=0.75,
            y=0.25,
            text='4',
            showarrow=False
        )
    ]
 )

fig = dict(data=[data], layout=layout)
py.iplot(fig, validate=False)