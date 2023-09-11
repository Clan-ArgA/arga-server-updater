from abc import ABC, abstractmethod


class ModSymlinkPort(ABC):
    @abstractmethod
    def create(self, mod_name: str, mod_id: str) -> str:
        """Create Mod Symlink."""
