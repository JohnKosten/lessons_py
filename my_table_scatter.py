import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

from bq_helper import BigQueryHelper
client = BigQueryHelper('bigquery-public-data','usa-names')

import plotly.graph_objects as go
from plotly.offline import plot

query = "select name, number from bigquery-public-data.usa_names.usa_1910_current limit 150"

df = client.query_to_pandas(query)

x = df['name']

y= df['number']

name =go.Scatter(x=x , y=y, mode="lines")

layout = go.Layout(title='Scatter' )

fig = go.Figure(data=[name], layout = layout)

plot(fig)