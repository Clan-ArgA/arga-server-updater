from server_updater.domain.miscellaneous.logger_repository import LoggerRepository


class LoggerAdapter(LoggerRepository):
    @staticmethod
    def info(msg: str) -> None:
        log_output = f"\n{'':=<{len(msg)}}\n{msg}\n{'':=<{len(msg)}}"
        print(log_output)

    @staticmethod
    def print(msg: str) -> None:
        """Print the message."""
        print(msg)
