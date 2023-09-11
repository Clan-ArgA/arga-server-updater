from server_updater.domain.miscellaneous.logger_port import LoggerPort
from server_updater.domain.mod_symlink.mod_symlink_service import ModSymlinkService


class CreateModSymlinksUseCase:
    def __init__(
        self,
        logger: LoggerPort,
        mod_symlink_service: ModSymlinkService,
    ):
        self._logger = logger
        self._mod_symlink_service = mod_symlink_service

    def create(self) -> bool:
        self._logger.print_head("Creating symlinks...")
        return self._mod_symlink_service.create()