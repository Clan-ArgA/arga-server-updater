from server_updater.domain.exceptions.decorators.generic_error_handler import (
    generic_error_handler,
)
from server_updater.domain.lower_case_mods.lower_case_mods_repository import (
    LowerCaseModsRepository,
)
from server_updater.domain.mod_symlink.mod_symlink_service import ModSymlinkService
from server_updater.domain.mods.mods_update_service import ModsUpdateService


class UpdateModsOnlyUseCase:
    def __init__(
        self,
        mods_update_service: ModsUpdateService,
        lower_case_mods_adapter: LowerCaseModsRepository,
        mod_symlink_service: ModSymlinkService,
    ):
        self._mods_update_service = mods_update_service
        self._lower_case_mods_adapter = lower_case_mods_adapter
        self._mod_symlink_service = mod_symlink_service

    @generic_error_handler
    def update(self) -> bool:
        self._mods_update_service.update()
        self._lower_case_mods_adapter.to_lower()
        self._mod_symlink_service.create()
        return True
