from rich.console import Console
from src.services.agent_service import fetch_agent_info, view_agent
from src.services.navigation_service import get_waypoint_info
from src.services.contract_service import view_contracts, accept_contract
from src.services.fleet_service import scan, get_in_orbit, dock, view_my_ships
from src.services.market_service import checkout_ships
from src.utils.logger import logger

console = Console()
logger.info("Starting SpaceTraders application...")

agent_info = fetch_agent_info()

waypoint_info = get_waypoint_info(agent_info=agent_info)
accepted = accept_contract("cm7fym8rd17k5s90kxc5mm9tb")

# console.print_json(data=view_my_ships())
console.print_json(data=get_in_orbit(shipSymbol="SUJAL_RJPT-1"))
logger.info("Application running successfully.")
