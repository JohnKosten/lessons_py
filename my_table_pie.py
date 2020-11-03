import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

import pandas as pd
from bq_helper import BigQueryHelper
client = BigQueryHelper('bigquery-public-data','usa-names')

import plotly.graph_objects as go
from plotly.offline import plot

query = "select name, number from bigquery-public-data.usa_names.usa_1910_current limit 25"

df = client.query_to_pandas(query)

fig = go.Figure( data=[go.Pie(labels=df['name'], values=df['number'])])
plot(fig)
