import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"


from google.cloud import bigquery

client = bigquery.Client()

dataset_reference = client.dataset('stackoverflow', project='bigquery-public-data')

print(type(dataset_reference))

datawarehouse_reference = client.get_dataset(dataset_reference)

for table in client.list_tables(datawarehouse_reference):
    print(table.table_id)


table_reference = client.get_table(datawarehouse_reference.table('users'))

print(table_reference.schema)