from unittest import TestCase, mock
from unittest.mock import MagicMock, patch

from server_updater.constants import Server
from server_updater.log import Log
from server_updater.main import ServerUpdater
from server_updater.steamcmd import SteamCmd


@mock.patch("server_updater.main.ServerUpdater._delete_mod_if_needed")
@mock.patch("server_updater.main.ServerUpdater._try_to_update_mod")
class TestMainCase(TestCase):
    def setUp(self) -> None:
        self._logger = MagicMock(spec=Log)
        self._steamcmd = MagicMock(spec=SteamCmd)
        self._a3_server_updater = ServerUpdater(
            logger=self._logger,
            steamcmd=self._steamcmd,
            server=Server.A3,
            mods_list_name=None)

    def test_update_mods_mod_needs_update_update_successful(self, try_to_update_mod, delete_mod_if_needed):
        expected = {"mod1": "12345", "mod2": "67890"}
        is_dir = True
        mod_needs_update = True
        delete_mod_if_needed.return_value = (is_dir, mod_needs_update)
        try_to_update_mod.return_value = True

        actual = self._a3_server_updater._update_mods(mods_to_update=expected)

        self.assertIsNotNone(actual)
        self.assertEqual(expected, actual)

    def test_update_mods_mod_needs_update_is_dir_false(self, try_to_update_mod, delete_mod_if_needed):
        expected = {"mod1": "12345", "mod2": "67890"}
        is_dir = False
        mod_needs_update = True
        delete_mod_if_needed.return_value = (is_dir, mod_needs_update)
        try_to_update_mod.return_value = True

        actual = self._a3_server_updater._update_mods(mods_to_update=expected)

        self.assertIsNotNone(actual)
        self.assertEqual(expected, actual)

