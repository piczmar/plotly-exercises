import numpy as np
import pandas as pd
import plotly as py
import plotly.figure_factory as FF
import plotly.graph_objs as go

# data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2010_alcohol_consumption_by_country.csv')
data = pd.read_csv('2010_alcohol_consumption_by_country.csv')
df = data[0:10]

# table = FF.create_table(df)
# py.offline.plot(table, filename='alcohol-data-sample.html')


mean = np.mean(data['alcohol'])
st_dev = np.std(data['alcohol'])

print ("The mean is %r" % mean)
print("The standard deviation is %r" % st_dev)

median = np.median(data['alcohol'])
maximum = np.max(data['alcohol'])
minimum = np.min(data['alcohol'])

print("The median is %r" % median)
print("The maximum is %r" % maximum)
print("The minimum is %r" % minimum)


# --------------------------------------------------
y = data['alcohol'].values.tolist()

fig = FF.create_violin(y, title='Violin Plot', colors='#604d9e')
py.offline.plot(fig, filename='alcohol-violin-visual.html')

# --------------------------------------------------
# https://plot.ly/python/box-plots/
y = data['alcohol'].values.tolist()

trace = go.Box(
    y=y,
    name = 'Box Plot',
    boxpoints='all',
    jitter=0.3,
    marker = dict(
        color = 'rgb(214,12,140)',
    ),
)

layout = go.Layout(
    width=500,
    yaxis=dict(
        title='Alcohol Consumption by Country',
        zeroline=False
    ),
)

data = [trace]
fig= go.Figure(data=data, layout=layout)
py.offline.plot(fig, filename='alcohol-box-plot.html')

# --------------------------------------------------