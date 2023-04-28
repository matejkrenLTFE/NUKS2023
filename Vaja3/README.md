Vaja 2: API

## About
- **Description**:
Preprost API za TODO aplikacijo.

## Development and testing
- **Set up developing enviroment** (only the first time):
    - `pyenv local 3.11.2`
    - `python -m venv .venv`
    - `source .venv/bin/activate`
    - `pip install -r requirements.txt`

- **Development:**
    - Before running the following commands activate the virtual enviroment: `source .venv/bin/activate`. 
    - To deactivate enter `deactivate`.
    - Run app locally: `uvicorn main:app --reload --host 0.0.0.0`

