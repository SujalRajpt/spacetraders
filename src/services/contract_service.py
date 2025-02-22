from src.config import BASE_URL, HEADERS
import requests


def view_contracts():
    """Fetch agent's active contracts."""
    url = f"{BASE_URL}/my/contracts"
    response = requests.get(url, headers=HEADERS)
    return response.json()
