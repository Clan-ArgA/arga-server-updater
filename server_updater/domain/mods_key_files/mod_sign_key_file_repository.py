from abc import ABC, abstractmethod


class ModSignKeyFileRepository(ABC):
    @staticmethod
    @abstractmethod
    def copy() -> str:
        """Copy the Mods sign files."""
