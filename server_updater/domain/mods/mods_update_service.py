from server_updater.domain.exceptions.decorators.generic_error_handler import (
    generic_error_handler,
)
from server_updater.domain.mods.mods_repocitory import ModRepository
from server_updater.domain.mods.mods_update_repository import ModsUpdateRepository


class ModsUpdateService:
    def __init__(
        self, mod_update_repository: ModsUpdateRepository, mods: ModRepository
    ):
        self._mod_update = mod_update_repository
        self._mods = mods

    @generic_error_handler
    def update(self) -> bool:
        mods = self._mods.get()
        for mod_name, mod_id in mods.items():
            self._mod_update.update(mod_name=mod_name, mod_id=mod_id)
        return True
