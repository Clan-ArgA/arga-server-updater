from unittest import TestCase
from unittest.mock import MagicMock, patch

from server_updater.config import A3_WORKSHOP_DIR
from server_updater.constants import Server
from server_updater.log import Log
from server_updater.main import ServerUpdater
from server_updater.steamcmd import SteamCmd


@patch("shutil.rmtree")
@patch("server_updater.main.ServerUpdater._mod_needs_update")
@patch("os.path.isdir")
class TestServerA3MainCase(TestCase):
    def setUp(self) -> None:
        self.mock_logger = MagicMock(spec=Log)
        self.mock_steamcmd = MagicMock(spec=SteamCmd)
        self._a3_server_updater = ServerUpdater(
            logger=self.mock_logger,
            steamcmd=self.mock_steamcmd,
            server=Server.A3,
            mods_list_name=None,
        )

    def test_server_a3_update_mods_mod_not_installed(
        self, mock_isdir, mock_mod_needs_update, mock_rmtree
    ):
        mock_isdir.side_effect = [False, False, True]
        mock_mod_needs_update.return_value = True
        mock_rmtree.return_value = ""
        mods = {"mod_1": "620260972"}
        expected = mods
        expected_call = f"{A3_WORKSHOP_DIR}/620260972"

        actual = self._a3_server_updater._update_mods(mods_to_update=mods, time_sleep=0)

        self.assertEqual(expected, actual)
        mock_isdir.assert_called_with(expected_call)
        # mock_mod_needs_update.assert_called_with("620260972", expected_call)
        mock_rmtree.assert_not_called()

    def test_server_a3_update_mods_mod_installed_no_update_needed(
        self, mock_isdir, mock_mod_needs_update, mock_rmtree
    ):
        mock_isdir.return_value = True
        mock_mod_needs_update.return_value = False
        mock_rmtree.return_value = ""
        mods = {"mod_1": "620260972"}
        expected = None
        expected_call = f"{A3_WORKSHOP_DIR}/620260972"

        actual = self._a3_server_updater._update_mods(mods_to_update=mods, time_sleep=0)

        self.assertEqual(expected, actual)
        mock_isdir.assert_called_with(expected_call)
        mock_mod_needs_update.assert_called_with("620260972", expected_call)
        mock_rmtree.assert_not_called()

    def test_server_a3_update_mods_mod_installed_update_needed(
        self, mock_isdir, mock_mod_needs_update, mock_rmtree
    ):
        mock_isdir.side_effect = [True, False, True]
        mock_mod_needs_update.return_value = True
        mock_rmtree.return_value = ""
        mods = {"mod_1": "620260972"}
        expected = mods
        expected_call = f"{A3_WORKSHOP_DIR}/620260972"

        actual = self._a3_server_updater._update_mods(mods_to_update=mods, time_sleep=0)

        self.assertEqual(expected, actual)
        mock_isdir.assert_called_with(expected_call)
        mock_mod_needs_update.assert_called_with("620260972", expected_call)
        mock_rmtree.assert_called_with(expected_call)

    def test_mod_not_installed_download_fails_after_10_tries(
        self, mock_isdir, mock_mod_needs_update, mock_rmtree
    ):
        mock_isdir.side_effect = [False] * 12
        mock_mod_needs_update.return_value = False
        mock_rmtree.return_value = ""
        mods = {"mod_1": "620260972"}
        expected = None
        expected_call = f"{A3_WORKSHOP_DIR}/620260972"

        actual = self._a3_server_updater._update_mods(mods_to_update=mods, time_sleep=0)

        self.assertEqual(expected, actual)
        mock_isdir.assert_called_with(expected_call)
        mock_mod_needs_update.assert_not_called()
        mock_rmtree.assert_not_called()

    def test_mod_needs_update_download_succeeds_after_5_tries(
        self, mock_isdir, mock_mod_needs_update, mock_rmtree
    ):
        mock_isdir.side_effect = [True] + [False] * 5 + [True]
        mock_mod_needs_update.return_value = True
        mock_rmtree.return_value = ""
        mods = {"mod_1": "620260972"}
        expected = mods
        expected_call = f"{A3_WORKSHOP_DIR}/620260972"

        actual = self._a3_server_updater._update_mods(mods_to_update=mods, time_sleep=0)

        self.assertEqual(expected, actual)
        mock_isdir.assert_called_with(expected_call)
        mock_mod_needs_update.assert_called_with("620260972", expected_call)
        mock_rmtree.assert_called_with(expected_call)
