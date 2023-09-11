from server_updater.domain.miscellaneous.logger_repository import LoggerRepository
from server_updater.domain.mod_symlink.mod_symlink_repository import (
    ModSymlinkRepository,
)
from server_updater.domain.mods.mods_repository import ModRepository


class ModSymlinkService:
    def __init__(
        self,
        logger: LoggerRepository,
        mods_repository: ModRepository,
        mod_symlink_repository: ModSymlinkRepository,
    ):
        self._mods_repository = mods_repository
        self._logger = logger
        self._mod_symlink_repository = mod_symlink_repository

    def create(self) -> bool:
        """Create Mod Symlink."""
        self._logger.print_head("Creating symlinks...")
        mods = self._mods_repository.list_mods()
        for mod_name, mod_id in mods.items():
            response = self._mod_symlink_repository.create(
                mod_name=mod_name, mod_id=mod_id
            )
            if response is not None:
                self._logger.print(response)
        return True
