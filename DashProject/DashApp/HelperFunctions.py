import pandas as pd
import re
import os
import dash
import dash_core_components as dcc
import dash_html_components as html

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'static_files','HumanDevelopmentIndexSummaryStatistics.csv')

df = pd.read_csv(filename)

l = []
length = len(df.columns)

for i in range(0,length):
  x = re.findall('^U',df.columns[i])
  if x:
    l.append(i)

df1 = df.drop(columns=[df.columns[i] for i in l])
col={}
years = [i for i in range(1990,2020)]
altyears = [df1.columns[i] for i in range(1,31)]

for i in range(0,30):
  col[altyears[i]] = years[i]
col[df1.columns[0]]=df1.columns[0]

df2=df1.rename(columns=col)
df3=df2.drop(index=5)
df3=df3.set_index('Human Development')
df3_T=df3.T

HDI = df3_T


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
