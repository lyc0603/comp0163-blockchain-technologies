"""
Script to query The Graph API for data on DeFi protocols and pools.
"""

from pprint import pprint

import requests

url = 'https://gateway.thegraph.com/api/deployments/id/QmdEuhCPTFx5q1Vf7jPQDVGQDpC34KYry82yb3NPc9sK6a'

headers = {
    'accept': 'application/json, multipart/mixed',
    'accept-language': 'en',
    'authorization': 'Bearer 944b560e76f53abf0739468966998887',
    'content-type': 'application/json',
    'origin': 'https://thegraph.com',
    'priority': 'u=1, i',
    'referer': 'https://thegraph.com/',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

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