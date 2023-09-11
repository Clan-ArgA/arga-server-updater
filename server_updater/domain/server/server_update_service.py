from server_updater.config import A3_SERVER_ID
from server_updater.domain.constants import UpdateType
from server_updater.domain.exceptions.decorators.generic_error_handler import (
    generic_error_handler,
)
from server_updater.domain.miscellaneous.logger_port import LoggerPort
from server_updater.domain.steam_command.steam_command_port import (
    SteamCommandPort,
)


class ServerUpdateService:
    def __init__(self, logger: LoggerPort, steamcmd: SteamCommandPort):
        self._logger = logger
        self._steamcmd = steamcmd

    @generic_error_handler
    def update(self) -> bool:
        self._logger.print_head(f"Updating A3 server ({A3_SERVER_ID})")
        self._steamcmd.run(UpdateType.SERVER)
        return True
