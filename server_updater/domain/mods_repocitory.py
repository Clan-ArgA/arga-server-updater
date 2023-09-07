from abc import ABC, abstractmethod
from typing import Dict


class ModRepository(ABC):
    @staticmethod
    @abstractmethod
    def get() -> Dict[str, str]:
        """Get the Mods"""
