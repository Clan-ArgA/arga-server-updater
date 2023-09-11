from server_updater.applications.lower_case_mods_use_case import LowerCaseModsUseCase
from server_updater.infrastructure.adapters.logger_terminal_adapter import LoggerTerminalAdapter
from server_updater.infrastructure.adapters.lower_case_mods_os_adapter import (
    LowerCaseModsOsAdapter,
)


class LowerCaseModsUseCaseWiring:
    @staticmethod
    def instantiate() -> LowerCaseModsUseCase:
        return LowerCaseModsUseCase(
            lower_case_mods=LowerCaseModsOsAdapter(),
            logger=LoggerTerminalAdapter(),
        )
