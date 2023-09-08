from server_updater.domain.miscellaneous.logger_repository import LoggerRepository
from server_updater.domain.mods_key_files.mod_sign_key_file_repository import (
    ModSignKeyFileRepository,
)


class ModSignKeyFileService:
    def __init__(
        self, sign_repository: ModSignKeyFileRepository, logger: LoggerRepository
    ):
        self._sign_repository = sign_repository
        self._logger = logger

    def copy(self) -> str:
        result = self._sign_repository.copy()
        self._logger.print(result)
        return result
