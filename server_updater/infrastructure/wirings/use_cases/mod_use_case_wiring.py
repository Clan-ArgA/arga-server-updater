from server_updater.applications.update_mods_only_use_case import UpdateModsOnlyUseCase
from server_updater.config import (
    A3_WORKSHOP_DIR,
    WORKSHOP_CHANGELOG_URL,
    MOD_KEYS_SOURCE_DIRECTORY,
    MOD_KEYS_DESTINATION_DIRECTORY,
)
from server_updater.domain.mod_symlink.mod_symlink_repository import (
    ModSymlinkRepository,
)
from server_updater.domain.mod_symlink.mod_symlink_service import ModSymlinkService
from server_updater.domain.mods.mods_update_repository import ModsUpdateRepository
from server_updater.domain.mods.mods_update_service import ModsUpdateService
from server_updater.domain.mods_key_files.mod_sign_key_file_service import (
    ModSignKeyFileService,
)
from server_updater.infrastructure.adapters.logger_terminal_adapter import LoggerTerminalAdapter
from server_updater.infrastructure.adapters.lower_case_mods_os_adapter import (
    LowerCaseModsOsAdapter,
)
from server_updater.infrastructure.adapters.mod_sign_key_file_adapter import (
    ModSignKeyFileAdapter,
)
from server_updater.infrastructure.adapters.mod_symlink_adapter import ModSymlinkAdapter
from server_updater.infrastructure.adapters.mods_adapter import ModAdapter
from server_updater.infrastructure.adapters.mods_update_adapter import ModsUpdateAdapter
from server_updater.infrastructure.wirings.steamcmd_wiring import SteamcmdWiring


class ModUseCaseWiring:
    def instantiate(self) -> UpdateModsOnlyUseCase:
        return UpdateModsOnlyUseCase(
            mods_update_service=self._mods_update_service,
            lower_case_mods_adapter=LowerCaseModsOsAdapter(),
            mod_symlink_service=self._mod_symlink_service,
            sign_key_service=self._sign_key_service,
        )

    @property
    def _mods_update_service(self) -> ModsUpdateService:
        return ModsUpdateService(
            mod_update_repository=self._mod_update_repository, mods_repository=ModAdapter()
        )

    @property
    def _mod_update_repository(self) -> ModsUpdateRepository:
        return ModsUpdateAdapter(
            logger=LoggerTerminalAdapter(),
            steamcmd=SteamcmdWiring().instantiate(),
            mods_repository=ModAdapter(),
            a3_workshop_dir=A3_WORKSHOP_DIR,
            workshop_changelog_url=WORKSHOP_CHANGELOG_URL,
        )

    @property
    def _mod_symlink_service(self) -> ModSymlinkService:
        return ModSymlinkService(
            logger=LoggerTerminalAdapter(),
            mods_repository=ModAdapter(),
            mod_symlink_repository=self._mod_symlink_repository,
        )

    @property
    def _mod_symlink_repository(self) -> ModSymlinkRepository:
        return ModSymlinkAdapter(
            a3_workshop_dir=A3_WORKSHOP_DIR,
            workshop_changelog_url=WORKSHOP_CHANGELOG_URL,
        )

    @property
    def _sign_key_service(self) -> ModSignKeyFileService:
        return ModSignKeyFileService(
            sign_repository=self._sign_repository,
            logger=LoggerTerminalAdapter(),
        )

    @property
    def _sign_repository(self) -> ModSignKeyFileAdapter:
        return ModSignKeyFileAdapter(
            source_directory=MOD_KEYS_SOURCE_DIRECTORY,
            destination_directory=MOD_KEYS_DESTINATION_DIRECTORY,
        )
