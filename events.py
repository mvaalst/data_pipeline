import pandas as pd
import json
from google.cloud import bigquery

# Read the JSON file
file_path = 'data/events.json'
with open(file_path, 'r') as file:
    json_data = json.load(file)

# flatten JSON data due to nested structure
flattened_data = []

for event in json_data:
# Extract event-level fields
    event_details = {
        'group_id': event.get('group_id'),
        'name': event.get('name'),
        'description': event.get('description'),
        'created': event.get('created'),
        'time': event.get('time'),
        'duration': event.get('duration'),
        'rsvp_limit': event.get('rsvp_limit'),
        'venue_id': event.get('venue_id'),
        'status': event.get('status')
    }
    
    for rsvp in event['rsvps']:
        if isinstance(rsvp, dict):  # Ensure each RSVP is a dictionary
            rsvp_details = event_details.copy()  # Copy event details into RSVP record
            rsvp_details['user_id'] = rsvp.get('user_id')
            rsvp_details['when'] = rsvp.get('when')
            rsvp_details['response'] = rsvp.get('response')
            rsvp_details['guests'] = rsvp.get('guests')
            
            flattened_data.append(rsvp_details)
        else:
            print(f"Invalid RSVP format: {rsvp}")

dataframe = pd.DataFrame(flattened_data)

# Upload the dataframe to BigQuery
client = bigquery.Client()
table_id = 'striped-torus-445510-c9.raw_data.events'

job = client.load_table_from_dataframe(dataframe, table_id, job_config=bigquery.LoadJobConfig(
                                        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE))
job.result()
print(f"Data successfully loaded into {table_id}")