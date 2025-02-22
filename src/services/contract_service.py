from src.config import BASE_URL, HEADERS
import requests


def view_contracts():
    """Fetch agent's active contracts."""
    url = f"{BASE_URL}/my/contracts"
    response = requests.get(url, headers=HEADERS)
    return response.json()


def accept_contract(contract_id):
    url = f"{BASE_URL}/my/contracts/{contract_id}/accept"
    response = requests.post(url, headers=HEADERS)
    return response.json
