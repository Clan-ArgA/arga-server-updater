import os
import sys
from typing import Optional, Dict, Any

from server_updater.dtos import ServerConfig
from server_updater.config import (
    STEAM_CMD,
    STEAM_USER,
    STEAM_PASS,
    A3_SERVER_DIR,
    A3_SERVER_ID,
    A3_WORKSHOP_ID,
    REFORGER_SERVER_ID,
    REFORGER_SERVER_DIR,
)
from server_updater.constants import UpdateType, Server


class SteamCmd:
    def __init__(self, server: Server):
        self._server = server
        self._config = self._set_config()

    def run(self, update_type: UpdateType, mod_id: Optional[int] = None) -> None:
        params = self._get_params().get(update_type, self._error_type)(mod_id)
        os.system(f"{STEAM_CMD} {params}")
        print("")

    def _get_update_server_params(self, mod_id: Optional[int] = None) -> str:
        steam_cmd_params = self._steam_cmd_params
        steam_cmd_params += f" +app_update {self._config.server_id} validate"
        steam_cmd_params += " +quit"
        return steam_cmd_params

    def _get_update_mod_params(self, mod_id: int) -> str:
        steam_cmd_params = self._steam_cmd_params
        steam_cmd_params += f" +workshop_download_item {A3_WORKSHOP_ID} {mod_id}"
        steam_cmd_params += " validate +quit"
        return steam_cmd_params

    @staticmethod
    def _error_type(mod_id: Optional[int] = None) -> str:
        print("ERROR: update_type name is incorrect")
        sys.exit()

    def _get_params(self) -> Dict[UpdateType, Any]:
        return {
            UpdateType.SERVER: self._get_update_server_params,
            UpdateType.MOD: self._get_update_mod_params,
        }

    @property
    def _steam_cmd_params(self) -> str:
        steam_cmd_params = f" +force_install_dir {self._config.server_dir}"
        steam_cmd_params += f" +login {STEAM_USER} {STEAM_PASS}"
        return steam_cmd_params

    def _set_config(self):
        if self._server == Server.A3:
            return ServerConfig(server_id=A3_SERVER_ID, server_dir=A3_SERVER_DIR)
        return ServerConfig(
            server_id=REFORGER_SERVER_ID, server_dir=REFORGER_SERVER_DIR
        )
