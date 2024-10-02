"""
Script to introduce the cryptocompare API
"""
import json

import matplotlib.pyplot as plt
import pandas as pd

from environ.data_fetcher import get_daily_pair_ohlcv
from environ.constants import DATA, CC_API_KEY

# get the price history of BTC
btc_json = get_daily_pair_ohlcv(fsym="BTC", tsym="USD", limit=2000, api_key=CC_API_KEY)

# save the json to a file
with open(
    f"{DATA}/btc.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(btc_json, f)

# convert the json to a pandas dataframe
btc_df = pd.DataFrame(btc_json["Data"]["Data"])

# convert the time to a datetime object
btc_df["time"] = pd.to_datetime(btc_df["time"], unit="s")

# visualize the close price
plt.figure(figsize=(8, 3))
plt.plot(btc_df["time"], btc_df["close"])
plt.xlabel("Time")
plt.ylabel("Price (USD)")
plt.title("Bitcoin Close Price History")
plt.show()
