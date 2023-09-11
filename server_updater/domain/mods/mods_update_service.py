from typing import Dict

from server_updater.domain.exceptions.decorators.generic_error_handler import (
    generic_error_handler,
)
from server_updater.domain.mods.mods_repository import ModRepository
from server_updater.domain.mods.mods_update_port import ModsUpdatePort


class ModsUpdateService:
    def __init__(
        self, mod_update_port: ModsUpdatePort, mods_port: ModRepository
    ):
        self._mod_update = mod_update_port
        self._mods_port = mods_port

    @generic_error_handler
    def update(self) -> bool:
        mods = self._mods_port.list_mods_by_steam_id()
        for mod_id, mod_name in mods.items():
            self._mod_update.update(mod_name=mod_name, mod_id=mod_id)
        return True

    @generic_error_handler
    def save_mods_to_file(self, file_name: str, mods: Dict[str, Dict[str, str]]) -> None:
        self._mods_port.save_mods_to_json(file_name=file_name, mods=mods)
