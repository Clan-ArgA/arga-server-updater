from server_updater.domain.lower_case_mods.lower_case_mods_port import (
    LowerCaseModsPort,
)
from server_updater.infrastructure.adapters.logger_terminal_adapter import (
    LoggerTerminalAdapter,
)


class LowerCaseModsUseCase:
    def __init__(
        self, lower_case_mods: LowerCaseModsPort, logger: LoggerTerminalAdapter
    ):
        self._lower_case_mods = lower_case_mods
        self._logger = logger

    def to_lower(self) -> None:
        self._logger.print_head("Converting uppercase files/folders to lowercase...")
        self._lower_case_mods.to_lower()
