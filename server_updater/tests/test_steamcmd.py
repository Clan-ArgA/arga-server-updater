from unittest import TestCase
from unittest.mock import patch

from server_updater.config import STEAM_USER, STEAM_PASS
from server_updater.constants import UpdateType, Server
from server_updater.steamcmd import SteamCmd


@patch("os.system")
class SteamCmdTest(TestCase):
    def setUp(self) -> None:
        self._arma3_expected = (
            f"/home/arma/steamcmd/steamcmd.sh  "
            f"+force_install_dir /home/arma/steamcmd/arma3 "
            f"+login {STEAM_USER} {STEAM_PASS}"
        )

        self._reforger_expected = (
            f"/home/arma/steamcmd/steamcmd.sh  "
            f"+force_install_dir /home/arma/steamcmd/reforger "
            f"+login {STEAM_USER} {STEAM_PASS}"
        )

    def test_a3_steamcmd_server(self, mock_system):
        expected = f"{self._arma3_expected} +app_update 233780 validate +quit"
        steamcmd = SteamCmd(server=Server.A3)
        steamcmd.run(update_type=UpdateType.SERVER)
        mock_system.assert_called_with(expected)

    def test_a3_steamcmd_mod(self, mock_system):
        expected = (
            f"{self._arma3_expected} +workshop_download_item 107410 620260972 validate +quit"
        )
        steamcmd = SteamCmd(server=Server.A3)
        steamcmd.run(update_type=UpdateType.MOD, mod_id=620260972)
        mock_system.assert_called_with(expected)

    def test_reforger_steamcmd_server(self, mock_system):
        expected = f"{self._reforger_expected} +app_update 1874900 validate +quit"
        steamcmd = SteamCmd(server=Server.REFORGER)
        steamcmd.run(update_type=UpdateType.SERVER)
        mock_system.assert_called_with(expected)
