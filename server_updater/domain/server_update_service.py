from server_updater.config import A3_SERVER_ID
from server_updater.domain.constants import UpdateType
from server_updater.domain.exceptions.decorators.generic_error_handler import (
    generic_error_handler,
)
from server_updater.domain.logger_repository import LoggerRepository
from server_updater.domain.steam_command_repository import SteamCommandRepository


class ServerUpdateService:
    def __init__(self, logger: LoggerRepository, steamcmd: SteamCommandRepository):
        self._logger = logger
        self._steamcmd = steamcmd

    @generic_error_handler
    def update(self) -> bool:
        self._logger.info(f"Updating A3 server ({A3_SERVER_ID})")
        self._steamcmd.run(UpdateType.SERVER)
        return True
