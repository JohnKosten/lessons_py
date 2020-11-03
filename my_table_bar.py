import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

import pandas as pd
from bq_helper import BigQueryHelper
client = BigQueryHelper('bigquery-public-data','usa-names')

import plotly.graph_objects as go
from plotly.offline import plot

query = "select name, number from bigquery-public-data.usa_names.usa_1910_current limit 150"

df = client.query_to_pandas(query)

bar = go.Bar(x = df['name'], y= df['number'] )

layout = go.Layout(title='Names', xaxis= dict(title = 'name') ,  yaxis= dict( title = 'number') )

fig = go.Figure(data = [bar], layout = layout )

plot(fig)
