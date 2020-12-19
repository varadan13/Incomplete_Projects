fig = go.Figure()
config = dict({'scrollZoom': False,'displayModeBar': False})
fig.add_trace(go.Scatter(x=np.array(df[df.columns[5]]),
                              y=np.array(df.index) ) )
fig.update({
    'layout': {
        'xaxis':{'range' :[0,1],'color': 'purple','title':'df'},
        'yaxis':{'range' :[1980,2020], 'color': 'purple','title':'dfd'},
        'title': 'haha',
        
                       }
            }) 

fig.show(config=config)