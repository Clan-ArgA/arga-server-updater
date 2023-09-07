from unittest import TestCase
from unittest.mock import patch

from server_updater.infrastructure.adapters.logger_adapter import LoggerAdapter


class Testlog(TestCase):
    @patch("builtins.print")
    def test_log(self, mock_print):
        logger = LoggerAdapter()
        logger.info("Test info message")
        mock_print.assert_called_with(
            "\n================\nTest info message\n================"
        )
