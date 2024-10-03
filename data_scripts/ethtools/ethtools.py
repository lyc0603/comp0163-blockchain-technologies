"""
Script to fetch data from the Ethereum blockchain using the web3 library
"""

from web3 import HTTPProvider, Web3

from environ.constants import DATA, INFURA_API_KEY
from environ.data_fetcher import FunctionCaller

# connect to a remote node
infuraurl = f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"
w3 = Web3(HTTPProvider(infuraurl))


ABIDIR = f"{DATA}/abi.json"
address = "0xc3d688B66703497DAA19211EEdff47f25384cdc3"

contract = FunctionCaller(address, w3, ABIDIR)
on_chain_data = contract.call_function("getReserves")
print(on_chain_data)
