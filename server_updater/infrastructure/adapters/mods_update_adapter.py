import os
import shutil
import time
from datetime import datetime
from urllib import request

from server_updater.config import PATTERN
from server_updater.domain.constants import UpdateType
from server_updater.domain.i_o_repository import IORepository
from server_updater.domain.logger_repository import LoggerRepository
from server_updater.domain.mods_repocitory import ModRepository
from server_updater.domain.mods_update_repository import ModsUpdateRepository
from server_updater.domain.steam_command_repository import SteamCommandRepository


class ModsUpdateAdapter(ModsUpdateRepository):
    def __init__(
        self,
        logger: LoggerRepository,
        steamcmd: SteamCommandRepository,
        mods: ModRepository,
        input_output: IORepository,
        a3_workshop_dir: str,
        workshop_changelog_url: str,
    ):
        self._logger = logger
        self._steamcmd = steamcmd
        self._mods = mods
        self._input_output = input_output
        self._a3_workshop_dir = a3_workshop_dir
        self._workshop_changelog_url = workshop_changelog_url

    def update(self, mod_name: str, mod_id: str) -> bool:
        """Update."""
        path = f"{self._a3_workshop_dir}/{mod_id}"

        # Check if mod needs to be updated
        if os.path.isdir(path):
            if self._mod_needs_update(mod_id, path):
                # Delete existing folder so that we can verify whether the download succeeded
                shutil.rmtree(path)
            else:
                print(f'No update required for "{mod_name}" ({mod_id})... SKIPPING')
                return False
        self._steamcmd.run(UpdateType.MOD_SHORT)

        # Keep trying until the download actually succeeded
        tries = 0
        while os.path.isdir(path) is False and tries < 10:
            self._logger.info(f'Updating "{mod_name}" ({mod_id}) | {tries + 1}')
            self._steamcmd.run(UpdateType.MOD)
            # Sleep for a bit so that we can kill the script if needed
            time.sleep(5)
            tries += 1

        if tries >= 10:
            self._logger.info(f"!! Updating {mod_name} failed after {tries} tries !!")

        return True

    def _mod_needs_update(self, mod_id, path) -> bool:
        if not os.path.isdir(path):
            return False
        match = self._get_mod_status(mod_id)
        if not match:
            return False
        updated_at = datetime.fromtimestamp(int(match.group(1)))
        created_at = datetime.fromtimestamp(os.path.getctime(path))
        return updated_at >= created_at

    def _get_mod_status(self, mod_id):
        response = request.urlopen(f"{self._workshop_changelog_url}/{mod_id}").read()
        response = response.decode("utf-8")
        return PATTERN.search(response)
