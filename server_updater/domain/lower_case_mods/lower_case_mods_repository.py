from abc import ABC, abstractmethod


class LowerCaseModsRepository(ABC):
    @staticmethod
    @abstractmethod
    def to_lower() -> None:
        """Converts the name of each mod to lowercase text."""
