from server_updater.applications.update_mods_only_use_case import UpdateModsOnlyUseCase
from server_updater.config import A3_WORKSHOP_DIR, WORKSHOP_CHANGELOG_URL
from server_updater.domain.mod_symlink.mod_symlink_repository import (
    ModSymlinkRepository,
)
from server_updater.domain.mod_symlink.mod_symlink_service import ModSymlinkService
from server_updater.domain.mods.mods_update_repository import ModsUpdateRepository
from server_updater.domain.mods.mods_update_service import ModsUpdateService
from server_updater.infrastructure.adapters.logger_adapter import LoggerAdapter
from server_updater.infrastructure.adapters.lower_case_mods_adapter import (
    LowerCaseModsAdapter,
)
from server_updater.infrastructure.adapters.mod_symlink_adapter import ModSymlinkAdapter
from server_updater.infrastructure.adapters.mods_adapter import ModAdapter
from server_updater.infrastructure.adapters.mods_update_adapter import ModsUpdateAdapter
from server_updater.infrastructure.wirings.steamcmd_wiring import SteamcmdWiring


class ModUseCaseWiring:
    def instantiate(self) -> UpdateModsOnlyUseCase:
        return UpdateModsOnlyUseCase(
            mods_update_service=self._mods_update_service,
            lower_case_mods_adapter=LowerCaseModsAdapter(),
            mod_symlink_service=self._mod_symlink_service,
        )

    @property
    def _mods_update_service(self) -> ModsUpdateService:
        return ModsUpdateService(
            mod_update_repository=self._mod_update_repository, mods=ModAdapter()
        )

    @property
    def _mod_update_repository(self) -> ModsUpdateRepository:
        return ModsUpdateAdapter(
            logger=LoggerAdapter(),
            steamcmd=SteamcmdWiring().instantiate(),
            mods=ModAdapter(),
            a3_workshop_dir=A3_WORKSHOP_DIR,
            workshop_changelog_url=WORKSHOP_CHANGELOG_URL,
        )

    @property
    def _mod_symlink_service(self) -> ModSymlinkService:
        return ModSymlinkService(
            logger=LoggerAdapter(),
            mods=ModAdapter(),
            mod_symlink_repository=self._mod_symlink_repository,
        )

    @property
    def _mod_symlink_repository(self) -> ModSymlinkRepository:
        return ModSymlinkAdapter(
            a3_workshop_dir=A3_WORKSHOP_DIR,
            workshop_changelog_url=WORKSHOP_CHANGELOG_URL,
        )
