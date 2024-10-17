# comp0163-blockchain-technologies
COMP0163 Blockchain Technologies Teaching Materials

[![python](https://img.shields.io/badge/Python-%3E%203.9.0-3776AB.svg?style=flat&logo=python&logoColor=white
)](https://www.python.org)

# Table of Contents

- Lab 1: Data Fetching
    - Introduction to the Lab, Blockchain, and Cryptocurrency.
    - Traget of this lab (practice, technical foundation, and project management).
    - Data fetching
    - Why we need these data? (academic and industrial)
    - API, web scraping, and develepment tools.
- Lab 2: Bitcoin Testnet Transaction
    - Crawl and monitor the evolution of the Ethereum repository in GitHub. (Fundamental, EVM, DeFi)
    - Get pseudo Bitcoin and send transactions on the Bitcoin testnet
- Lab 3: Permissioned Blockchain
    - Introduction to DAML
    - DAML project for space listing
    - DAML project for cash simple
    - DAML project for coworking full
# Structure
```
comp0163-blockchain-technologies/
├── data/               # Folder to store raw data    
├── data_scripts/       # Folder for Lab 1: Data Fetching
│   ├── cryptocompare/      # Off-chain data (crypto price, volume, mcap) fetching scripts
│   ├── eth_tools/           # On-chain data (decentralized protocols) fetching via web3 library
│   ├── bigql/              # On-chain data (bitcoin txn) fetching via BigQuery
│   └── thegraph/           # On-chain data (decentralized protocols) fetching via TheGraph
├── test_btc/           # Folder for Lab 2: Bitcoin Testnet Transaction
│   ├── TestBTC-2024.ipynb  # Jupyter notebook for Lab 2
├── daml/               # Folder for Lab 3: Permissioned Blockchain
│   ├── space_listing      # DAML project for space listing
│   ├── cash_simple        # DAML project for cash simple
│   ├── coworking_full    # DAML project for coworking full
├── environ/            # Folder to store utils
│   ├── constants.py        # Constants such as path and API keys
│   ├── data_fetcher.py     # Data fetching functions
│   └── settings.py         # Project root path
├── .gitignore          # Git ignore file
├── LICENSE             # License file
├── README.md           # README file
├── pyproject.toml      # Configuration file
└── setup_repo.sh       # Setup script
```


# Setup
```zsh
git clone https://github.com/lyc0603/comp0163-blockchain-technologies.git
cd comp0163-blockchain-technologies
```

### Give execute permission to your script and then run `setup_repo.sh`

- MacOS / Linux

```
chmod +x setup_repo.sh
./setup_repo.sh
. venv/bin/activate
```

or follow the step-by-step instructions below between the two horizontal rules:

---

#### Create a python virtual environment

- MacOS / Linux

```bash
python3 -m venv venv
```

- Windows

```bash
python -m venv venv
```

#### Activate the virtual environment

- MacOS / Linux

```bash
. venv/bin/activate
```

- Windows (in Command Prompt, NOT Powershell)

```bash
venv\Scripts\activate.bat
```
#### Install toml

```
pip install toml
```

#### Install the project in editable mode

```bash
pip install -e ".[dev]"
```

#### Install pre-commit
```bash
pre-commit install
```

#### Update the code

```bash
git pull
```
