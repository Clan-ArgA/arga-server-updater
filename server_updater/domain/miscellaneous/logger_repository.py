from abc import ABC, abstractmethod


class LoggerRepository(ABC):
    @staticmethod
    @abstractmethod
    def print_head(msg: str) -> None:
        """Print the message between two lines of =."""

    @staticmethod
    @abstractmethod
    def print(msg: str) -> None:
        """Print the message."""
