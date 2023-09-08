from server_updater.applications.mod_segn_key_file_use_case import ModSignKeyFileUseCase
from server_updater.config import (
    MOD_KEYS_SOURCE_DIRECTORY,
    MOD_KEYS_DESTINATION_DIRECTORY,
)
from server_updater.domain.mods_key_files.mod_sign_key_file_service import (
    ModSignKeyFileService,
)
from server_updater.infrastructure.adapters.logger_adapter import LoggerAdapter
from server_updater.infrastructure.adapters.mod_sign_key_file_adapter import (
    ModSignKeyFileAdapter,
)


class ModSignKeyFileUseCaseWiring:
    def instantiate(self) -> ModSignKeyFileUseCase:
        return ModSignKeyFileUseCase(sign_key_service=self._sign_key_service())

    def _sign_key_service(self) -> ModSignKeyFileService:
        return ModSignKeyFileService(
            sign_repository=self._sign_repository,
            logger=LoggerAdapter(),
        )

    @property
    def _sign_repository(self) -> ModSignKeyFileAdapter:
        return ModSignKeyFileAdapter(
            source_directory=MOD_KEYS_SOURCE_DIRECTORY,
            destination_directory=MOD_KEYS_DESTINATION_DIRECTORY,
        )
