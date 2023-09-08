from server_updater.domain.miscellaneous.logger_repository import LoggerRepository
from server_updater.domain.mod_symlink.mod_symlink_repository import (
    ModSymlinkRepository,
)
from server_updater.domain.mods.mods_repocitory import ModRepository


class ModSymlinkService:
    def __init__(
        self,
        logger: LoggerRepository,
        mods: ModRepository,
        mod_symlink_repository: ModSymlinkRepository,
    ):
        self._mods = mods
        self._logger = logger
        self._mod_symlink_repository = mod_symlink_repository

    def create(self) -> bool:
        """Create Mod Symlink."""
        self._logger.info("Creating symlinks...")
        mods = self._mods.get()
        for mod_name, mod_id in mods.items():
            response = self._mod_symlink_repository.create(
                mod_name=mod_name, mod_id=mod_id
            )
            if response is None:
                continue
            self._logger.print(response)
        return True
