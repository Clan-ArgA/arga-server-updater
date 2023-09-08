from server_updater.domain.exceptions.decorators.generic_error_handler import (
    generic_error_handler,
)
from server_updater.domain.server.server_update_service import ServerUpdateService


class UpdateServerOnlyUseCase:
    def __init__(self, server_update_service: ServerUpdateService):
        self._server_update_service = server_update_service

    @generic_error_handler
    def update(self) -> bool:
        return self._server_update_service.update()
