from server_updater.domain.exceptions.decorators.generic_error_handler import (
    generic_error_handler,
)
from server_updater.domain.mods.mods_repository import ModRepository
from server_updater.domain.mods.mods_update_repository import ModsUpdateRepository


class ModsUpdateService:
    def __init__(
        self, mod_update_repository: ModsUpdateRepository, mods_repository: ModRepository
    ):
        self._mod_update = mod_update_repository
        self._mods_repository = mods_repository

    @generic_error_handler
    def update(self) -> bool:
        mods = self._mods_repository.list_mods()
        for mod_name, mod_id in mods.items():
            self._mod_update.update(mod_name=mod_name, mod_id=mod_id)
        return True
