from src.config import BASE_URL, HEADERS
import requests


def get_waypoint_info(agent_info):
    """Fetch location details of the agent's current waypoint."""
    current_system = "-".join(agent_info["headquarters"].split("-")[:2])
    current_waypoint = agent_info["headquarters"]
    url = f"{BASE_URL}/systems/{current_system}/waypoints/{current_waypoint}"
    response = requests.get(url, headers=HEADERS)
    return response.json()
