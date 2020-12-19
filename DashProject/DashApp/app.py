import os
import sys
path=os.path.join(os.getcwd(),'DashProject')
sys.path.append(path)
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from DashApp.HelperFunctions import HDI,generate_table
import dash
import dash_core_components as dcc
import dash_html_components as html




df = HDI

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='HDI'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)





