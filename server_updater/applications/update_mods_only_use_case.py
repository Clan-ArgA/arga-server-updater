from typing import Dict

from server_updater.domain.exceptions.decorators.generic_error_handler import (
    generic_error_handler,
)
from server_updater.domain.lower_case_mods.lower_case_mods_port import (
    LowerCaseModsPort,
)
from server_updater.domain.mod_symlink.mod_symlink_service import ModSymlinkService
from server_updater.domain.mods.mods_update_service import ModsUpdateService
from server_updater.domain.mods_key_files.mod_sign_key_file_service import (
    ModSignKeyFileService,
)


class UpdateModsOnlyUseCase:
    def __init__(
        self,
        mods_update_service: ModsUpdateService,
        lower_case_mods_adapter: LowerCaseModsPort,
        mod_symlink_service: ModSymlinkService,
        sign_key_service: ModSignKeyFileService,
    ):
        self._mods_update_service = mods_update_service
        self._lower_case_mods_adapter = lower_case_mods_adapter
        self._mod_symlink_service = mod_symlink_service
        self._sign_key_service = sign_key_service

    @generic_error_handler
    def update(self) -> bool:
        self._mods_update_service.update()
        self._lower_case_mods_adapter.to_lower()
        self._mod_symlink_service.create()
        self._sign_key_service.copy()
        return True

    @generic_error_handler
    def update_and_save(self, file_name: str, mods: Dict[str, Dict[str, str]]) -> bool:
        self._save_mods_to_file(file_name=file_name, mods=mods)
        self.update()
        return True

    @generic_error_handler
    def _save_mods_to_file(self, file_name: str, mods: Dict[str, Dict[str, str]]) -> None:
        self._mods_update_service.save_mods_to_file(file_name=file_name, mods=mods)



