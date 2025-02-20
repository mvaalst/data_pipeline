import pandas as pd
import json
from google.cloud import bigquery

# Read the JSON file and load it into a dataframe
file_path = '.data/venues.json'
with open(file_path, 'r') as file:
    json_data = json.load(file)

dataframe = pd.DataFrame(json_data)

# Upload the dataframe to BigQuery
client = bigquery.Client()
table_id = 'striped-torus445510-c9.raw_data.venues'

job = client.load_table_from_dataframe(dataframe, table_id, job_config=bigquery.LoadJobConfig(
                                        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE))
job.result()
print(f"Data successfully loaded into {table_id}")
