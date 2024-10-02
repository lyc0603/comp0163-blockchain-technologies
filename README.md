# comp0163-blockchain-technologies
COMP0163 Blockchain Technologies Teaching Materials

[![python](https://img.shields.io/badge/Python-v3.11.2-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
<!-- [![build status](https://github.com/pre-commit/pre-commit/actions/workflows/main.yml/badge.svg)](https://github.com/xujiahuayz/pbs/actions/workflows/pylint.yml) -->

# Structure
```
comp0163-blockchain-technologies/
├── data/               # Folder to store raw data    
├── data_scripts/       # Folder for Lab 1: Data Fetching
│   ├── cryptocompare/      # Off-chain data fetching scripts
│   ├── ethtools/           # On-chain data fetching via Ethereum Tools
│   ├── bigql/              # On-chain data fetching via BigQuery
│   └── thegraph/           # On-chain data fetching via TheGraph
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
