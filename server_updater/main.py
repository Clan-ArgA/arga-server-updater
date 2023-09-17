import os
import shutil
import sys
import time
from datetime import datetime
from typing import Dict, Any
from urllib import request

from dtos import ServerConfig
from server_updater.config import (
    A3_SERVER_ID,
    A3_MODS_DIR,
    A3_WORKSHOP_DIR,
    A3_MOD_KEYS_SOURCE_DIRECTORY,
    A3_MOD_KEYS_DESTINATION_DIRECTORY,
    WORKSHOP_CHANGELOG_URL,
    PATTERN,
    REFORGER_SERVER_ID, REFORGER_ARMA_BINARY, REFORGER_ARMA_PROFILE, REFORGER_ARMA_MAX_FPS, REFORGER_ARMA_CONFIG,
)
from server_updater.constants import UpdateType, Server
from server_updater.log import Log
from server_updater.mods import MODS
from server_updater.steamcmd import SteamCmd


class ServerUpdater:
    def __init__(self, logger: Log, steamcmd: SteamCmd, server: Server):
        self._logger = logger
        self._steamcmd = steamcmd
        self._server = server
        self._config = self._set_config()

    def run(self):
        choices = self._get_choices()
        while True:
            selected = self._input()
            choices[self._server].get(selected.lower(), self._default)()

    def _input(self) -> str:
        return input(self._get_input_choices())

    def _get_input_choices(self) -> str:
        input_map = {
            Server.A3: """
                      A: Update server and Mods
                      B: Update Mods only
                      C: Update Server only
                      D: Create mod symlinks
                      E: Lower case mods
                      F: Copy key files
                      Q: Quit/Log Out
                      Please enter your choice: """,
            Server.REFORGER: """
                      A: Update Server only
                      B: Run Reforger server 
                      Q: Quit/Log Out
                      Please enter your choice: """,
        }
        return input_map[self._server]

    def _update_server_and_mods(self):
        self._update_server()
        self._update_mods_only()

    def _update_mods_only(self) -> None:
        self._update_mods()
        self._lower_case_mods()
        self._create_mod_symlinks()
        self._copy_key_files()

    def _update_server(self) -> None:
        self._logger.log(
            f"Updating {self._server.value} server ({self._config.server_id})"
        )
        self._steamcmd.run(update_type=UpdateType.SERVER)

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

            # Keep trying until the download actually succeeded
            tries = 0
            while os.path.isdir(path) is False and tries < 10:
                self._logger.log(f'Updating "{mod_name}" ({mod_id}) | {tries + 1}')
                self._steamcmd.run(update_type=UpdateType.MOD, mod_id=mod_id)
                # Sleep for a bit so that we can kill the script if needed
                time.sleep(5)
                tries += 1

            if tries >= 10:
                self._logger.log(
                    f"!! Updating {mod_name} failed after {tries} tries !!"
                )

    def _copy_key_files(self):
        """Copy the Mods sign files."""

        # Find files with the .bikey extension in the source directory
        for root_dir, _, files in os.walk(A3_MOD_KEYS_SOURCE_DIRECTORY):
            for file in files:
                if not file.endswith(".bikey"):
                    continue
                source_file_path = os.path.join(root_dir, file)
                destination_file_path = os.path.join(
                    A3_MOD_KEYS_DESTINATION_DIRECTORY, file
                )
                # Copy the file to the destination folder
                shutil.copy(source_file_path, destination_file_path)

        return "Mods sign key files was successfully copied."

    @staticmethod
    def _run_reforger_server():
        # https://community.bistudio.com/wiki/Arma_Reforger:Startup_Parameters
        launch = " ".join(
            [
                REFORGER_ARMA_BINARY,
                f"-config {REFORGER_ARMA_CONFIG}",
                "-backendlog",
                "-nothrow",
                f"-maxFPS {REFORGER_ARMA_MAX_FPS}",
                f"-profile {REFORGER_ARMA_PROFILE}",
                os.environ["ARMA_PARAMS"],
            ]
        )
        print(launch, flush=True)
        os.system(launch)

    @staticmethod
    def _quit() -> None:
        print("\nClosing Program now")
        sys.exit()

    def _default(self) -> None:
        options = self._get_options_to_print()
        print()
        print(f"You must only select either {options} to quit.")
        print("Please try again")
        time.sleep(2)

    def _get_options_to_print(self) -> str:
        options = [o.upper() for o in self._get_choices()[self._server]]
        return f"{', '.join(options[:-1])} or {options[-1]}"

    def _get_choices(self) -> Dict[Server, Dict[str, Any]]:
        return {
            Server.A3: {
                "a": self._update_server_and_mods,
                "b": self._update_mods_only,
                "c": self._update_server,
                "d": self._create_mod_symlinks,
                "e": self._lower_case_mods,
                "f": self._copy_key_files,
                "q": self._quit,
            },
            Server.REFORGER: {
                "a": self._update_server,
                "b": self._run_reforger_server,
                "q": self._quit,
            },
        }

    def _set_config(self):
        if self._server == Server.A3:
            return ServerConfig(
                server_id=A3_SERVER_ID,
            )
        return ServerConfig(
            server_id=REFORGER_SERVER_ID,
        )
