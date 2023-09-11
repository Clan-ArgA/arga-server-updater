from abc import ABC, abstractmethod
from typing import Dict


class ModRepository(ABC):
    @staticmethod
    @abstractmethod
    def list_mods() -> Dict[str, str]:
        """Get the Mods"""
