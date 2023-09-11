from abc import ABC, abstractmethod
from typing import Dict


class ModRepository(ABC):
    @staticmethod
    @abstractmethod
    def list_mods_by_steam_id() -> Dict[str, str]:
        """List the Mods."""
