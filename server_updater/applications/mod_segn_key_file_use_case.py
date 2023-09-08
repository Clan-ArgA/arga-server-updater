from server_updater.domain.mods_key_files.mod_sign_key_file_service import (
    ModSignKeyFileService,
)


class ModSignKeyFileUseCase:
    def __init__(
        self,
        sign_key_service: ModSignKeyFileService,
    ):
        self._sign_key_service = sign_key_service

    def copy(self) -> None:
        self._sign_key_service.copy()
