"""
Script to query The Graph API for data on DeFi protocols and pools.
"""

from pprint import pprint

import requests

API_KEY = "YOUR_API_KEY"
url = "https://gateway.thegraph.com/api/subgraphs/id/8wR23o1zkS4gpLqLNU4kG3JHYVucqGyopL5utGxP2q1N"

headers = {"Authorization": f"Bearer {API_KEY}"}

data = {
    "query": """
    {
      protocols(first: 5) {
        id
        pools {
          id
        }
      }
      contractToPoolMappings(first: 5) {
        id
        pool {
          id
        }
      }
    }
    """
}

response = requests.post(url, headers=headers, json=data)

pprint(response.json())
