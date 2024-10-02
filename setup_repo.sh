python3 -m venv venv;
source venv/bin/activate;
python3 -m pip install --upgrade pip;
pip install toml;
pip install -e ".[dev]";