from abc import ABC, abstractmethod
from typing import Dict


class ModRepository(ABC):
    @abstractmethod
    def list_mods_by_steam_id(self) -> Dict[str, str]:
        """List the Mods."""

    @abstractmethod
    def save_mods_to_json(self, file_name: str, mods: Dict[str, Dict[str, str]]) -> None:
        """Save the Mods to a JSON file."""
