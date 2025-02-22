from src.config import BASE_URL, HEADERS
import requests


def scan(agent_info, entity=""):
    traits = ""
    if len(entity) != 0:
        traits = f"?traits={entity}"
    current_system = "-".join(agent_info["headquarters"].split("-")[:2])
    url = f"{BASE_URL}/systems/{current_system}/waypoints{traits}"
    response = requests.get(url, headers=HEADERS)
    return response.json()


def view_all_system():
    url = f"{BASE_URL}/systems"
    response = requests.get(url, headers=HEADERS)
    return response.json()


def view_my_ships():
    url = f"{BASE_URL}/my/ships"
    response = requests.get(url, headers=HEADERS)
    return response.json()


def get_in_orbit(shipSymbol):
    url = f"{BASE_URL}/my/ships/{shipSymbol}/orbit"
    response = requests.post(url, headers=HEADERS)
    return response.json()


def dock(shipSymbol):
    url = f"{BASE_URL}/my/ships/{shipSymbol}/dock"
    response = requests.post(url, headers=HEADERS)
    return response.json()
