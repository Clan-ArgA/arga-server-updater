import os
import shutil
import sys
import time
from datetime import datetime
from typing import Dict, Any
from urllib import request

from server_updater.config import (
    A3_SERVER_ID,
    A3_MODS_DIR,
    A3_WORKSHOP_DIR,
    WORKSHOP_CHANGELOG_URL,
    PATTERN,
)
from server_updater.constants import UpdateType
from server_updater.log import Log
from server_updater.mods import MODS
from server_updater.steamcmd import SteamCmd


class ServerUpdater:
    def __init__(self, logger: Log, steamcmd: SteamCmd):
        self._logger = logger
        self._steamcmd = steamcmd

    def run(self):
        choices = self._get_choices()
        while True:
            selected = self._show_options()
            choices.get(selected.lower(), self._default)()

    def _show_options(self) -> str:
        print()
        print()
        return self._input()

    def _update_server_and_mods(self):
        self._update_server()
        self._update_mods()
        self._lower_case_mods()
        self._create_mod_symlinks()

    @staticmethod
    def _input() -> str:
        return input(
            """
                      A: Update server and Mods
                      B: Update Mods only
                      C: Update Server only
                      D: Create mod symlinks
                      E: Lower case mods
                      Q: Quit/Log Out
                      Please enter your choice: """
        )

    def _update_mods_only(self) -> None:
        self._update_mods()
        self._lower_case_mods()
        self._create_mod_symlinks()

    def _update_server(self) -> None:
        self._logger.log(f"Updating A3 server ({A3_SERVER_ID})")
        self._steamcmd.run(UpdateType.SERVER)

    def _create_mod_symlinks(self) -> None:
        self._logger.log("Creating symlinks...")
        for mod_name, mod_id in MODS.items():
            link_path = f"{A3_MODS_DIR}/{mod_name}"
            real_path = f"{A3_WORKSHOP_DIR}/{mod_id}"

            if not os.path.isdir(real_path):
                print(f"Mod '{mod_name}' does not exist! ({real_path})")
                continue
            if os.path.islink(link_path):
                continue
            os.symlink(real_path, link_path)
            print(f"Creating symlink '{link_path}'...")

    def _lower_case_mods(self) -> None:
        self._logger.log("Converting uppercase files/folders to lowercase...")
        os.system(
            "(cd {} && find . -depth -exec rename -v 's/(.*)\/([^\/]*)/$1\/\L$2/' {{}} \;)".format(
                A3_WORKSHOP_DIR
            )
        )

    @staticmethod
    def _quit() -> None:
        print("Closing Program now")
        sys.exit()

    @staticmethod
    def _default() -> None:
        print()
        print("You must only select either A,B,C,D,E or Q to quit.")
        print("Please try again")
        time.sleep(2)

    def _get_choices(self) -> Dict[str, Any]:
        return {
            "a": self._update_server_and_mods,
            "b": self._update_mods_only,
            "c": self._update_server,
            "d": self._create_mod_symlinks,
            "e": self._lower_case_mods,
            "q": self._quit,
        }

    @staticmethod
    def _mod_needs_update(mod_id, path) -> bool:
        if not os.path.isdir(path):
            return False
        response = request.urlopen(f"{WORKSHOP_CHANGELOG_URL}/{mod_id}").read()
        response = response.decode("utf-8")
        match = PATTERN.search(response)

        if not match:
            return False
        updated_at = datetime.fromtimestamp(int(match.group(1)))
        created_at = datetime.fromtimestamp(os.path.getctime(path))
        return updated_at >= created_at

    def _update_mods(self) -> None:
        for mod_name, mod_id in MODS.items():
            path = f"{A3_WORKSHOP_DIR}/{mod_id}"

            # Check if mod needs to be updated
            if os.path.isdir(path):
                if self._mod_needs_update(mod_id, path):
                    # Delete existing folder so that we can verify whether the download succeeded
                    shutil.rmtree(path)
                else:
                    print(f'No update required for "{mod_name}" ({mod_id})... SKIPPING')
                    continue
            self._steamcmd.run(UpdateType.MODS_ONLY)

            # Keep trying until the download actually succeeded
            tries = 0
            while os.path.isdir(path) is False and tries < 10:
                self._logger.log(f'Updating "{mod_name}" ({mod_id}) | {tries + 1}')
                self._steamcmd.run(UpdateType.MOD)
                # Sleep for a bit so that we can kill the script if needed
                time.sleep(5)
                tries += 1

            if tries >= 10:
                self._logger.log(
                    f"!! Updating {mod_name} failed after {tries} tries !!"
                )
