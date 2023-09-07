from abc import ABC, abstractmethod


class IORepository(ABC):
    @staticmethod
    @abstractmethod
    def input() -> str:
        """User input."""

    @staticmethod
    @abstractmethod
    def output(msg: str) -> None:
        """Print the message."""
