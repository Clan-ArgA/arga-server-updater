from abc import ABC, abstractmethod


class ModSymlinkRepository(ABC):
    @abstractmethod
    def create(self, mod_name: str, mod_id: str) -> str:
        """Create Mod Symlink."""
