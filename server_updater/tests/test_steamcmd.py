from unittest import TestCase
from unittest.mock import patch

from server_updater.constants import UpdateType
from server_updater.steamcmd import SteamCmd


class SteamCmdTest(TestCase):
    @patch("os.system")
    def test_steamcmd_server(self, mock_system):
        expected = "/home/steam/steamcmd/steamcmd.sh  +login argasteam wsx147zaqsteam +force_install_dir /home/steam/steamcmd/arma3 +app_update 233780 validate +quit"
        steamcmd = SteamCmd()
        steamcmd.run(update_type=UpdateType.SERVER)
        mock_system.assert_called_with(expected)

    @patch("os.system")
    def test_steamcmd_mod_short(self, mock_system):
        expected = "/home/steam/steamcmd/steamcmd.sh  +force_install_dir /home/steam/steamcmd/arma3 +quit"
        steamcmd = SteamCmd()
        steamcmd.run(update_type=UpdateType.MODS_ONLY)
        mock_system.assert_called_with(expected)

    @patch("os.system")
    def test_steamcmd_mod(self, mock_system):
        expected = "/home/steam/steamcmd/steamcmd.sh  +login argasteam wsx147zaqsteam +force_install_dir /home/steam/steamcmd/arma3 +workshop_download_item 107410 15 validate +quit"
        steamcmd = SteamCmd()
        steamcmd.run(update_type=UpdateType.MOD, mod_id=15)
        mock_system.assert_called_with(expected)
