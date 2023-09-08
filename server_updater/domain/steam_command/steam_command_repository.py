from abc import ABC, abstractmethod
from typing import Optional

from server_updater.domain.constants import UpdateType


class SteamCommandRepository(ABC):
    @abstractmethod
    def run(self, update_type: UpdateType, mod_id: Optional[int] = None) -> None:
        """Run the steamcmd with parameters"""
