from abc import ABC, abstractmethod


class LoggerRepository(ABC):
    @staticmethod
    @abstractmethod
    def info(msg: str) -> None:
        """Print the message between two lines of =."""
