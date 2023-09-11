from server_updater.domain.miscellaneous.logger_port import LoggerPort
from server_updater.domain.mods_key_files.mod_sign_key_file_port import (
    ModSignKeyFilePort,
)


class ModSignKeyFileService:
    def __init__(self, sign_repository: ModSignKeyFilePort, logger: LoggerPort):
        self._sign_repository = sign_repository
        self._logger = logger

    def copy(self) -> str:
        result = self._sign_repository.copy()
        self._logger.print(result)
        return result
