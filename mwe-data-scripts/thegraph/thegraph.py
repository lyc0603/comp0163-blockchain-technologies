"""
Script to query The Graph API for data on DeFi protocols and pools.
"""

from pprint import pprint

import requests

url = 'https://gateway.thegraph.com/api/deployments/id/QmdEuhCPTFx5q1Vf7jPQDVGQDpC34KYry82yb3NPc9sK6a'

headers = {}

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

if __name__ == '__main__':
  response = requests.post(url, headers=headers, json=data)
  pprint(response.json())