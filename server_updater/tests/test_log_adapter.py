from unittest import TestCase
from unittest.mock import patch

from server_updater.infrastructure.adapters.logger_terminal_adapter import (
    LoggerTerminalAdapter,
)


class TestlogAdapter(TestCase):
    @patch("builtins.print")
    def test_log(self, mock_print):
        logger = LoggerTerminalAdapter()
        logger.print_head("Test print_head message")
        mock_print.assert_called_with(
            "\n================\nTest print_head message\n================"
        )
