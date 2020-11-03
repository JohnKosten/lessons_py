import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

from bq_helper import BigQueryHelper
client = BigQueryHelper('bigquery-public-data','usa-names')



#query = "select * from bigquery-public-data.stackoverflow.stackoverflow_posts "

#df = client.query_to_pandas(query)

#df.sort_values('answer_count',ascending=False, inplace=True)
#result = df.iloc[:2]


# VS


query = "select * from bigquery-public-data.usa_names.usa_1910_current limit 1500"

df = client.query_to_pandas(query)

print(df)