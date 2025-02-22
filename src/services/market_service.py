from src.config import BASE_URL, HEADERS
import requests


def checkout_ships(shipyard_system, shipyard_waypoint):
    url = f"{BASE_URL}/systems/{shipyard_system}/waypoints/{shipyard_waypoint}/shipyard"
    response = requests.get(url, headers=HEADERS)
    return response.json()
