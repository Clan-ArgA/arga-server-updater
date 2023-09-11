from abc import ABC, abstractmethod


class ModSignKeyFilePort(ABC):
    @staticmethod
    @abstractmethod
    def copy() -> str:
        """Copy the Mods sign files."""
