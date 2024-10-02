"""
Script to fetch data from the Ethereum blockchain using the eth-tools package
"""

import json
from subprocess import PIPE, run

INFURA_API_KEY = "5434aa4866964dc6afc026cac5e7e20a"
infuraurl = f'https://mainnet.infura.io/v3/{INFURA_API_KEY}'

rootcommand = 'eth-tools call-contract'



# using https://github.com/danhper/ethereum-tools, run `pip install ethereum-tools` first


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
    ABIDIR = 'ctoken.json'
    cbatadd = '0x8164Cc65827dcFe994AB23944CBC90e0aa80bFcb'

    ttlbrw = get_contract_output(
        addr=cbatadd, func='totalBorrowsCurrent', abipath=ABIDIR)
    print(ttlbrw)
