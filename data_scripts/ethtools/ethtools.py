"""
Script to fetch data from the Ethereum blockchain using the eth-tools package
"""

from environ.data_fetcher import get_contract_output
from environ.constants import DATA, INFURA_API_KEY


infuraurl = f'https://mainnet.infura.io/v3/{INFURA_API_KEY}'


ABIDIR = f"{DATA}/abi.json"
address = '0xc3d688B66703497DAA19211EEdff47f25384cdc3'

on_chain_data = get_contract_output(
    addr=address, func='getReserves', abipath=ABIDIR, endpoint=infuraurl)
print(on_chain_data)
