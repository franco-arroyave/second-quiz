import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\josef\\AppData\\Roaming\\gcloud\\application_default_credentials.json"
os.environ["GCLOUD_PROJECT"] = "tech-fellowship-405004"

client = bigquery.Client()

# Perform a query.
QUERY = (
    'SELECT * '
    'FROM `bigquery-public-data.world_bank_intl_education.country_series_definitions` '
    'LIMIT 100')

query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row)