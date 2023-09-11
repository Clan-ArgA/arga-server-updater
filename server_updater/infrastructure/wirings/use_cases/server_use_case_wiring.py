from server_updater.applications.update_server_only_use_case import (
    UpdateServerOnlyUseCase,
)
from server_updater.domain.server.server_update_service import ServerUpdateService
from server_updater.infrastructure.adapters.logger_terminal_adapter import (
    LoggerTerminalAdapter,
)
from server_updater.infrastructure.wirings.steamcmd_wiring import SteamcmdWiring


class ServerUseCaseWiring:
    def instantiate(self) -> UpdateServerOnlyUseCase:
        return UpdateServerOnlyUseCase(
            server_update_service=self._server_update_service
        )

    @property
    def _server_update_service(self) -> ServerUpdateService:
        return ServerUpdateService(
            logger=LoggerTerminalAdapter(),
            steamcmd=SteamcmdWiring().instantiate(),
        )
