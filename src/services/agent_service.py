from src.config import BASE_URL, HEADERS
import requests


def fetch_agent_info():
    """Fetch agent's details including current system and waypoint."""
    url = f"{BASE_URL}/my/agent"
    response = requests.get(url, headers=HEADERS)
    return response.json()["data"]
