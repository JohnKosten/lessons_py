import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

import pandas as pd
from bq_helper import BigQueryHelper
client = BigQueryHelper('bigquery-public-data','stackoverflow')

query = "select id from bigquery-public-data.stackoverflow.posts where age is not null limit 1000"