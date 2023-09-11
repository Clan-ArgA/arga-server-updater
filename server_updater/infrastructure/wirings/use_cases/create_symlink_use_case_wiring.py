from server_updater.applications.create_mod_symlinks_use_case import (
    CreateModSymlinksUseCase,
)
from server_updater.domain.mod_symlink.mod_symlink_service import ModSymlinkService
from server_updater.infrastructure.adapters.logger_terminal_adapter import LoggerTerminalAdapter
from server_updater.infrastructure.adapters.mods_adapter import ConstanModAdapter
from server_updater.infrastructure.wirings.mods_symlink_wiring import ModSymlinkWiring


class CreateSymlinkUseCaseWiring:
    def instantiate(self) -> CreateModSymlinksUseCase:
        return CreateModSymlinksUseCase(
            logger=LoggerTerminalAdapter(), mod_symlink_service=self._mod_symlink_service
        )

    @property
    def _mod_symlink_service(self) -> ModSymlinkService:
        return ModSymlinkService(
            logger=LoggerTerminalAdapter(),
            mods_repository=ConstanModAdapter(),
            mod_symlink_repository=ModSymlinkWiring().instantiate(),
        )
