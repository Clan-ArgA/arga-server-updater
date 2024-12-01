import unittest
from unittest.mock import MagicMock, patch

from server_updater.constants import Server
from server_updater.main import ServerUpdater


class TestServerUpdater(unittest.TestCase):
    def setUp(self):
        self.mock_logger = MagicMock()
        self.mock_steamcmd = MagicMock()
        self.mock_server = MagicMock()

        self.server_updater = ServerUpdater(
            logger=self.mock_logger,
            steamcmd=self.mock_steamcmd,
            server=Server.A3,
            mods_list_name="mods_list",
            repair=None
        )

        self.server_updater._update_server_and_mods = MagicMock()
        self.server_updater._update_mods_only = MagicMock()
        self.server_updater._update_server = MagicMock()
        self.server_updater._quit = MagicMock()

    @patch.object(ServerUpdater, "_kill", return_value=None)
    def test_run_choice_valid_choice(self, mock_kill):
        selected_option = "a"
        self.server_updater.run_choice(selected_option)

        self.server_updater._update_server_and_mods.assert_called_once()
        mock_kill.assert_called_once()

    @patch.object(ServerUpdater, "_kill", return_value=None)
    def test_run_choice_quit_choice(self, mock_kill):
        selected_option = "q"
        self.server_updater.run_choice(selected_option)

        self.server_updater._quit.assert_called_once()
        mock_kill.assert_not_called()

    @patch.object(ServerUpdater, "_kill", return_value=None)
    def test_run_choice_invalid_choice(self, mock_kill):
        selected_option = "z"
        with self.assertRaises(KeyError):
            self.server_updater.run_choice(selected_option)

        self.server_updater._update_server_and_mods.assert_not_called()
        self.server_updater._update_mods_only.assert_not_called()
        self.server_updater._update_server.assert_not_called()
        self.server_updater._quit.assert_not_called()
        mock_kill.assert_not_called()

