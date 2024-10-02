"""
Script to fetch data from the Ethereum blockchain using the eth-tools package
"""

import json
from subprocess import PIPE, run

INFURA_API_KEY = "YOUR_INFURA_API_KEY"
infuraurl = f'https://mainnet.infura.io/v3/{INFURA_API_KEY}'

rootcommand = 'eth-tools call-contract'


def get_contract_output(
    addr: str, func: str, abipath: str, endpoint: str = infuraurl
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
    command = rootcommand + ' --abi ' + abipath + \
        ' --web3-uri ' + endpoint + ' -f ' + func + ' ' + addr
    print(command)

    output = run(command, shell=True, stdout=PIPE).stdout
    return json.loads(output)


if __name__ == "__main__":
    ABIDIR = 'mwe-data-scripts/ethtools/abi.json'
    address = '0xc3d688B66703497DAA19211EEdff47f25384cdc3'

    on_chain_data = get_contract_output(
        addr=address, func='getReserves', abipath=ABIDIR)
    print(on_chain_data)
