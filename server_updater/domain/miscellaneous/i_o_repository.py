from abc import ABC, abstractmethod
from typing import Optional


class IORepository(ABC):
    @staticmethod
    @abstractmethod
    def input() -> str:
        """User input."""

    @staticmethod
    @abstractmethod
    def output(msg: Optional[str] = "") -> None:
        """Print the message."""
