from typing import Dict

from server_updater.domain.mods.mods_repository import ModRepository
from server_updater.infrastructure.data.mods import MODS


class ModAdapter(ModRepository):
    @staticmethod
    def get() -> Dict[str, str]:
        """Get the URL"""
        return MODS
