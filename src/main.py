from rich.console import Console

from src.services.agent_service import fetch_agent_info
from src.services.navigation_service import get_waypoint_info
from src.services.contract_service import view_contracts

console = Console()

agent_info = fetch_agent_info()

waypoint_info = get_waypoint_info(agent_info=agent_info)
console.print_json(data=view_contracts())
