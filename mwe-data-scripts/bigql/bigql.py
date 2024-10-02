"""
Script to query BigQuery for Bitcoin transactions
"""
# run `pip install --upgrade google-cloud-bigquery` in the terminal first
import os

from google.cloud import bigquery
from pandas import json_normalize

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "mwe-data-scripts/bigql/YOUR_JSON_KEY_FILE.json"
client = bigquery.Client()

# Perform a query.
query_btc = ("""
select *,
from bigquery-public-data.crypto_bitcoin.transactions
WHERE block_timestamp_month = "2024-10-01"
LIMIT 1000
""")

query_job = client.query(query_btc)  # API request
rows = query_job.result()  # Waits for query to finish


field_names = [f.name for f in rows.schema]
# needs to be done in once, otherwise 'Iterator has already started' error
btc_tx_value = [{
    field: row[field] for field in field_names
} for row in rows]

print(json_normalize(btc_tx_value))