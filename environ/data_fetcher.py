"""
Functions for data fetching
"""

import json
from typing import Any, Optional

import requests
from web3 import Web3


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


class FunctionCaller:
    """
    Class to call functions from the smart contract
    """

    def __init__(self, contract_address: str, w3: Web3, abi_path: str):
        self.contract_address = contract_address
        self.w3 = w3
        self.abi_path = abi_path

    def _load_abi(
        self
    ) -> dict:
        """
        Function to load the abi of the smart contract

        Args:
            path (str): The path to the abi file

        Returns:    
            dict: The abi of the smart contract
        """

        with open(self.abi_path, "r", encoding="utf-8") as f:
            abi = json.load(f)

        return abi

    def _get_contract(
        self
    ) -> Any:
        """
        Function to get the contract object

        Returns:
            Any: The contract object
        """
        abi = self._load_abi()
        contract = self.w3.eth.contract(address=self.contract_address, abi=abi)
        return contract

    def call_function(
        self,
        function_name: str,
        block_identifier: int | str = "latest",
        params: Optional[Any] = None,
    ):
        """
        Function to call a function from the smart contract

        Args:
            function_name (str): The name of the function to call
            block_identifier (int | str, optional): The block number or 
                block hash to call the function at (default is 'latest').
            params (Optional[Any], optional): The parameters to pass 
                to the function (default is None).
        
        Returns:
            Any: The return value of the function
        """
        contract = self._get_contract()
        function = getattr(contract.functions, function_name)

        return (
            function().call(block_identifier=block_identifier)
            if params is None
            else function(*params).call(block_identifier=block_identifier)
        )