# Fetch on-chain data from BigQuery

- Author: Yichen Luo
- Date: 2024-10-01

## Dependencies

run following commands in the terminal first

```bash
pip install --upgrade google-cloud-bigquery
```

```Python
import os

from google.cloud import bigquery
from pandas import json_normalize
```

## Google BigQuery

Google BigQuery is a serverless, highly scalable, and cost-effective multi-cloud data warehouse designed for business agility. It enables super-fast SQL queries using the processing power of Google's infrastructure. BigQuery is a powerful tool for data analysis and visualization.

### Blockchain Data on BigQuery

Google BigQuery provides a dataset of blockchain data from various blockchains, including Bitcoin, Ethereum, and Litecoin. The dataset is updated regularly and contains a wealth of information about the blockchain, such as transactions, blocks, addresses, and more.

### Accessing Blockchain Data on BigQuery Playground

- Step 1: Go to the [Google Cloud Console](https://console.cloud.google.com/).
  
<img src="./fig/console.png" width="1400">

- Step 2: Create a new project or select an existing project.

<img src="./fig/new_project.png" width="1400">

<img src="./fig/project_settings.png" width="1400">

<img src="./fig/new_project.png" width="1400">

<img src="./fig/select_project.png" width="1400">


- Step 3: Enter the BigQuery console.

<img src="./fig/bigquery.png" width="1400">

- Step 4: Select the dataset you want to query.

<img src="./fig/select_dataset.png" width="1400">

- Step 5: Open the playground to run SQL queries.

<img src="./fig/playground.png" width="1400">

- Step 6: Write and run your SQL query to fetch blockchain data.

<img src="./fig/example_query.png" width="1400">

### Accessing Blockchain Data using API

- Step 1: Enter the credentials page.

<img src="./fig/credentials.png" width="1400">

<img src="./fig/service_acct.png" width="1400">

- Step 2: Create a service account.

<img src="./fig/service_acct_id.png" width="1400">

<img src="./fig/role_assign.png" width="1400">

<img src="./fig/select_acct.png" width="1400">

<img src="./fig/create_key.png" width="1400">

- Step 3: Download the JSON key file.

<img src="./fig/create_json.png" width="1400">


- Step 4: Put the JSON key file in your project directory.

### Fetching Blockchain Data using Python

```Python
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "YOUR_JSON_KEY_FILE.json"
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

json_normalize(btc_tx_value)
```
