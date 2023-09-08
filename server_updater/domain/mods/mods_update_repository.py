from abc import ABC


class ModsUpdateRepository(ABC):
    def update(self, mod_name: str, mod_id: str) -> bool:
        """Update."""
