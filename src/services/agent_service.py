from src.config import BASE_URL, HEADERS
import requests


def view_agent():
    """Fetch agent's details including current system and waypoint."""
    url = f"{BASE_URL}/my/agent"
    response = requests.get(url, headers=HEADERS)
    return response.json()


def fetch_agent_info():
    """Fetch agent's details including current system and waypoint."""
    url = f"{BASE_URL}/my/agent"
    response = requests.get(url, headers=HEADERS)
    return response.json()["data"]


def view_factions():
    url = f"{BASE_URL}/factions"
    response = requests.get(url, headers=HEADERS)
    return response.json()
