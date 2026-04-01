# PSU Python

A python package for abstracting python class methods behind a fully functional layer. Intended for educational use in CMPSC 131 at The Pennsylvania State University

## Usage

psu-python is packaged and available on PyPi. To use psu-python, install it with pip in your python environment:

```bash
pip install psu-python
```

You will now be able to import psu-python modules in your python code:

```python
# import all functions
from psu_python import *
# or specific ones
from psu_python import to_lower, get_item

def main():
    ...
```

## Developer Install

1. Clone the repository

   ```bash
   git clone git@github.com:tedtasman/psu-python.git
   cd ./psu-python
   ```

2. Create a virtual environment
   - MacOS / Linux:
     ```bash
     python3 -m venv .venv
     source ./.venv/bin/activate
     ```
   - Windows Powershell
     ```Powershell
     python -m venv .venv
     .\.venv\Scripts\activate
     ```

3. Install psu-python locally in editable mode
   ```bash
   pip install -e .
   ```
