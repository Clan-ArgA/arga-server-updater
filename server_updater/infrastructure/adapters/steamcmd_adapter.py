import os
from typing import Optional, Dict, Any

from server_updater.config import (
    STEAM_CMD,
    A3_SERVER_DIR,
    A3_SERVER_ID,
    A3_WORKSHOP_ID,
)
from server_updater.domain.constants import UpdateType
from server_updater.domain.exceptions.decorators.generic_error_handler import (
    generic_error_handler,
)
from server_updater.domain.exceptions.steamcmd_exceptions import UpdateTypeException
from server_updater.domain.steam_command.steam_command_repository import (
    SteamCommandRepository,
)


class SteamCmd(SteamCommandRepository):
    def __init__(self, steam_user: str, steam_pass: str):
        self._steam_user = steam_user
        self._steam_pass = steam_pass

    @generic_error_handler
    def run(self, update_type: UpdateType, mod_id: Optional[int] = None) -> None:
        try:
            params = self._get_params()[update_type](mod_id)
            os.system(f"{STEAM_CMD} {params}")
        except KeyError:
            raise UpdateTypeException(update_type=update_type)

    def _get_update_server_params(self, mod_id: Optional[int] = None) -> str:
        steam_cmd_params = self._steam_cmd_params
        steam_cmd_params += f" +app_update {A3_SERVER_ID} validate"
        steam_cmd_params += " +quit"
        return steam_cmd_params

    def _get_update_mod_params(self, mod_id: int) -> str:
        steam_cmd_params = self._steam_cmd_params
        steam_cmd_params += f" +workshop_download_item {A3_WORKSHOP_ID} {mod_id}"
        steam_cmd_params += " validate +quit"
        return steam_cmd_params

    def _get_params(self) -> Dict[UpdateType, Any]:
        return {
            UpdateType.SERVER: self._get_update_server_params,
            UpdateType.MOD: self._get_update_mod_params,
        }

    @property
    def _steam_cmd_params(self) -> str:
        steam_cmd_params = f" +force_install_dir {A3_SERVER_DIR}"
        steam_cmd_params += f" +login {self._steam_user} {self._steam_pass}"
        return steam_cmd_params
