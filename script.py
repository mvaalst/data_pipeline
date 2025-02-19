from google.cloud import bigquery
import pandas as pd
        
# Initialize the BigQuery client
client = bigquery.Client()

# Define the query string
query = """
  SELECT *
  FROM `striped-torus-445510-c9.football_stats.bundesliga_fixtures_2024_2025`
  LIMIT 10
"""

# Execute the query and fetch the results as a DataFrame
df = client.query(query).to_dataframe()

# Print the first 5 rows of the DataFrame
print(df.head())
