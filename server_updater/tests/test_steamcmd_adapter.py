from unittest import TestCase
from unittest.mock import patch

from server_updater.domain.constants import UpdateType
from server_updater.infrastructure.adapters.steamcmd_adapter import SteamCmd


class SteamCmdTest(TestCase):
    def setUp(self) -> None:
        self._steamcmd = SteamCmd(
            steam_user="user",
            steam_pass="pass",
        )
        self._expected = "/home/steam/steamcmd/steamcmd.sh  "
        self._expected += "+force_install_dir /home/steam/steamcmd/arma3"
        self._expected += f" +login user pass"

    @patch("os.system")
    def test_steamcmd_server(self, mock_system):
        expected = f"{self._expected} +app_update 233780 validate +quit"
        self._steamcmd.run(update_type=UpdateType.SERVER)
        mock_system.assert_called_with(expected)

    @patch("os.system")
    def test_steamcmd_mod(self, mock_system):
        expected = f"{self._expected} +workshop_download_item 107410 15 validate +quit"
        self._steamcmd.run(update_type=UpdateType.MOD, mod_id=15)
        mock_system.assert_called_with(expected)
