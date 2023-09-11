from abc import ABC


class ModsUpdatePort(ABC):
    def update(self, mod_name: str, mod_id: str) -> bool:
        """Update."""
