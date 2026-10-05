"""
Script to introduce the public Coinbase Exchange API (no API key needed).
"""

import json

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

from environ.data_fetcher import get_daily_pair_ohlcv
from environ.constants import DATA

# Search from 2010 and return all available BTC-USD history on Coinbase.
btc_json = get_daily_pair_ohlcv(fsym="BTC", tsym="USD", start_date="2010-01-01")

# save the json to a file
DATA.mkdir(parents=True, exist_ok=True)
with open(
    DATA / "btc_coinbase.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(btc_json, f)

# convert the json to a pandas dataframe
btc_df = pd.DataFrame(btc_json)

# convert the time to a datetime object
btc_df["time"] = pd.to_datetime(btc_df["time"], unit="s", utc=True)

# visualize the close price
plt.figure(figsize=(8, 3))
plt.plot(btc_df["time"], btc_df["close"])
plt.xlabel("Time (UTC)")
plt.ylabel("Price (USD)")
plt.title("Bitcoin Close Price History (Coinbase BTC-USD)")
plt.show()

# Draw daily candlesticks and volume from the same Coinbase data.
# Show the full history on both figures; set an integer for a shorter window.
candlestick_days = None
chart_df = btc_df if candlestick_days is None else btc_df.tail(candlestick_days)
dates = mdates.date2num(chart_df["time"].tolist())
colors = [
    "#16816a" if close >= open_price else "#c44e52"
    for open_price, close in zip(chart_df["open"], chart_df["close"])
]

fig, (price_ax, volume_ax) = plt.subplots(
    2,
    1,
    sharex=True,
    figsize=(14, 7),
    gridspec_kw={"height_ratios": [3, 1]},
    constrained_layout=True,
)
# The wick spans low to high; the body spans open to close.
price_ax.vlines(dates, chart_df["low"], chart_df["high"], colors=colors)
price_ax.bar(
    dates,
    (chart_df["close"] - chart_df["open"]).abs(),
    bottom=chart_df[["open", "close"]].min(axis=1),
    width=0.6,
    color=colors,
    edgecolor=colors,
)
# Show a horizontal body when open and close are equal (a doji).
for date, open_price, close, color in zip(
    dates, chart_df["open"], chart_df["close"], colors
):
    if open_price == close:
        price_ax.hlines(open_price, date - 0.3, date + 0.3, color=color)

volume_ax.bar(dates, chart_df["volume"], width=0.6, color=colors)
price_ax.set_title(
    f"Bitcoin Daily Candlesticks (Coinbase BTC-USD, {len(chart_df)} candles)"
)
price_ax.set_ylabel("Price (USD)")
volume_ax.set_ylabel("Volume (BTC)")
volume_ax.set_xlabel("Time (UTC)")
locator = mdates.AutoDateLocator(minticks=4, maxticks=8)
volume_ax.xaxis.set_major_locator(locator)
volume_ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))
for ax in (price_ax, volume_ax):
    ax.grid(axis="y", alpha=0.25)
plt.show()
