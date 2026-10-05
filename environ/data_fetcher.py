"""
Functions for data fetching
"""

import json
from datetime import datetime, timedelta, timezone
from time import sleep
from typing import Any, Optional
from urllib.parse import quote

import requests
from web3 import Web3


def get_daily_pair_ohlcv(
    fsym: str,
    tsym: str = "USD",
    limit: Optional[int] = None,
    start_date: str = "2010-01-01",
) -> list[dict]:
    """Fetch available Coinbase daily history from start_date through yesterday.

    Only pairs listed on Coinbase Exchange are supported. No API key is needed.
    With limit=None, search from start_date (YYYY-MM-DD); dates before trading
    began return no candles. Set limit to a positive integer to fetch only the
    last limit completed UTC days instead.
    Return records with time (Unix seconds), low, high, open, close, and volume
    (in the base asset), sorted by time. Days without trades may be absent.
    """
    if limit is not None and (
        isinstance(limit, bool) or not isinstance(limit, int) or limit <= 0
    ):
        raise ValueError("limit must be a positive integer number of days.")
    fsym, tsym = fsym.strip().upper(), tsym.strip().upper()
    if not fsym or not tsym:
        raise ValueError("fsym and tsym must be non-empty currency symbols.")

    product_id = f"{fsym}-{tsym}"
    url = (
        "https://api.exchange.coinbase.com/products/"
        f"{quote(product_id, safe='')}/candles"
    )
    # Exclude today's candle because its OHLCV values are still changing.
    end = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    if limit is None:
        start = datetime.strptime(start_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        if start >= end:
            raise ValueError("start_date must be before today's UTC date.")
    else:
        start = end - timedelta(days=limit)
    cursor = start
    candles = {}

    with requests.Session() as session:
        while cursor < end:
            # 299 days leaves room for an inclusive endpoint (300 candles).
            batch_end = min(cursor + timedelta(days=299), end)
            response = session.get(
                url,
                params={
                    "granularity": 86400,
                    "start": cursor.isoformat(),
                    "end": batch_end.isoformat(),
                },
                timeout=60,
            )
            response.raise_for_status()
            batch = response.json()
            if not isinstance(batch, list):
                raise ValueError(
                    f"Unexpected Coinbase response for {product_id}: {batch}"
                )

            for candle in batch:
                if not isinstance(candle, list) or len(candle) != 6:
                    raise ValueError(f"Unexpected Coinbase candle: {candle}")
                timestamp = int(candle[0])
                # The API can return candles outside the requested batch.
                if cursor.timestamp() <= timestamp < batch_end.timestamp():
                    candles[timestamp] = {
                        "time": timestamp,
                        **dict(
                            zip(
                                ("low", "high", "open", "close", "volume"),
                                map(float, candle[1:]),
                            )
                        ),
                    }

            cursor = batch_end
            if cursor < end:
                sleep(0.2)

    if not candles:
        raise ValueError(
            f"No daily candles returned for {product_id} in the requested period."
        )
    return [candles[timestamp] for timestamp in sorted(candles)]


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
