from unittest import TestCase
from unittest.mock import patch

from server_updater.infrastructure.adapters.logger_adapter import LoggerAdapter


class TestlogAdapter(TestCase):
    @patch("builtins.print")
    def test_log(self, mock_print):
        logger = LoggerAdapter()
        logger.print_head("Test print_head message")
        mock_print.assert_called_with(
            "\n================\nTest print_head message\n================"
        )
