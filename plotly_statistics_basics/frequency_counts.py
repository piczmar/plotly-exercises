import numpy as np
import pandas as pd
import plotly as py
import plotly.figure_factory as FF
import plotly.graph_objs as go

x = np.random.weibull(1.25, size=1000)
print(x[:10])

trace = [
  go.Histogram(x=x,
               xbins=dict(start=np.min(x), size=0.25, end=np.max(x)),
               marker=dict(color='rgb(0, 0, 100)'))
]

layout = go.Layout(
    title="Histogram Frequency Counts"
)

fig = go.Figure(trace, layout=layout)
py.offline.plot(fig, filename='histogram-freq-counts.html')

# ------------------------------------------

wind_data = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/wind_speed_laurel_nebraska.csv')
df = wind_data[0:10]

table = FF.create_table(df)
py.offline.plot(table)

data = [
  go.Histogram(
      x=wind_data['10 Min Std Dev'],
      histnorm='probability'
  )
]
py.offline.plot(data, filename='wind-data-histogram.html')
