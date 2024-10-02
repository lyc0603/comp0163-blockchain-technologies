"""
Functions for data fetching
"""

import requests
import json
from subprocess import PIPE, run


def get_daily_pair_ohlcv(fsym: str, tsym: str, limit: int, api_key: str) -> dict:
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
    BASEURL = "https://min-api.cryptocompare.com/data/v2/histoday?"
    url = (
        f"{BASEURL}fsym={fsym}&tsym={tsym}&limit={limit}&allData=true&api_key={api_key}"
    )

    # return the json response
    return requests.get(url, timeout=60).json()

def get_contract_output(
    addr: str, func: str, abipath: str, endpoint: str
):
    """
    Function to call a contract function and return the output

    Args:
        addr (str): Address of the contract
        func (str): Function to call
        abipath (str): Path to the ABI file
        endpoint (str): URL of the Ethereum node

    Returns:
        dict: Output of the contract function
    """
    rootcommand = 'eth-tools call-contract'

    command = rootcommand + ' --abi ' + abipath + \
        ' --web3-uri ' + endpoint + ' -f ' + func + ' ' + addr
    print(command)

    output = run(command, shell=True, stdout=PIPE).stdout
    return json.loads(output)