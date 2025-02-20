import pandas as pd
import json
from google.cloud import bigquery

# Read the JSON file
file_path = 'data/users.json'
with open(file_path, 'r') as file:
    json_data = json.load(file)

# flatten JSON data due to nested structure
flattened_data = []
for user in json_data:
    # Extract user-level fields
    user_details = {
        'user_id': user.get('user_id'),
        'city': user.get('city'),
        'country': user.get('country'),
        'hometown': user.get('hometown')
    }
    
    for memberships in user['memberships']:
        if isinstance(memberships, dict):  # Ensure each RSVP is a dictionary
            membership_details = user_details.copy()
            membership_details['joined'] = memberships.get('joined')
            membership_details['group_id'] = memberships.get('group_id')
            
            flattened_data.append(membership_details)
        else:
            print(f"Invalid membership format: {memberships}")

dataframe = pd.DataFrame(flattened_data)

# Upload the dataframe to BigQuery
client = bigquery.Client()
table_id = 'striped-torus-445510-c9.raw_data.users'

job = client.load_table_from_dataframe(dataframe, table_id, job_config=bigquery.LoadJobConfig(
                                        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE))
job.result()
print(f"Data successfully loaded into {table_id}")