from server_updater.domain.miscellaneous.logger_port import LoggerPort


class LoggerTerminalAdapter(LoggerPort):
    @staticmethod
    def print_head(msg: str) -> None:
        log_output = f"\n{'':=<{len(msg)}}\n{msg}\n{'':=<{len(msg)}}"
        print(log_output)

    @staticmethod
    def print(msg: str) -> None:
        """Print the message."""
        print(msg)
