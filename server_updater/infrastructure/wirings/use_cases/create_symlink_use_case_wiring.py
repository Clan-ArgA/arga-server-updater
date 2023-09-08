from server_updater.applications.create_mod_symlinks_use_case import (
    CreateModSymlinksUseCase,
)
from server_updater.domain.mod_symlink.mod_symlink_service import ModSymlinkService
from server_updater.infrastructure.adapters.logger_adapter import LoggerAdapter
from server_updater.infrastructure.adapters.mods_adapter import ModAdapter
from server_updater.infrastructure.wirings.mods_symlink_wiring import ModSymlinkWiring


class CreateSymlinkUseCaseWiring:
    def instantiate(self) -> CreateModSymlinksUseCase:
        return CreateModSymlinksUseCase(
            logger=LoggerAdapter(), mod_symlink_service=self._mod_symlink_service
        )

    @property
    def _mod_symlink_service(self) -> ModSymlinkService:
        return ModSymlinkService(
            logger=LoggerAdapter(),
            mods=ModAdapter(),
            mod_symlink_repository=ModSymlinkWiring().instantiate(),
        )
