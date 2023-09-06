from unittest import TestCase
from unittest.mock import patch

from server_updater.log import Log


class Testlog(TestCase):
    @patch('builtins.print')
    def test_log(self, mock_print):
        logger = Log()
        logger.log("Test log message")
        mock_print.assert_called_with("\n================\nTest log message\n================")
