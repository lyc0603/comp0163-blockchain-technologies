"""
Script to introduce the cryptocompare API
"""
import json

import matplotlib.pyplot as plt
import pandas as pd
import requests

BASEURL = "https://min-api.cryptocompare.com/data/v2/histoday?"
API_KEY = "YOUR_API_KEY"


def get_daily_pair_ohlcv(fsym: str, tsym: str = "USD", limit: int = 2000) -> dict:
    """
    Function to fetch daily OHLCV data of a cryptocurrency pair from cryptocompare API

    Args:
        fsym (str): The symbol of the cryptocurrency to retrieve data for (e.g., 'BTC' for Bitcoin).
        tsym (str, optional): The symbol of the currency to compare against (default is 'USD').
        limit (int, optional): The maximum number of data points to retrieve (default is 2000).
    
    Returns:
        dict: A dictionary containing the OHLCV data fetched from the CryptoCompare API. The 
              structure of the dictionary follows the CryptoCompare API's response format.
    """

    # construct the url
    url = f"{BASEURL}fsym={fsym}&tsym={tsym}&limit={limit}&allData=true&api_key={API_KEY}"

    # return the json response
    return requests.get(url, timeout=60).json()


if __name__ == "__main__":

    # get the price history of BTC
    btc_json = get_daily_pair_ohlcv(fsym="BTC")

    # save the json to a file
    with open(
        "btc.json",
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
