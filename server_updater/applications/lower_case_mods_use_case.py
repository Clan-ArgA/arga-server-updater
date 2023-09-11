from server_updater.domain.lower_case_mods.lower_case_mods_repository import (
    LowerCaseModsRepository,
)
from server_updater.infrastructure.adapters.logger_adapter import LoggerAdapter


class LowerCaseModsUseCase:
    def __init__(self, lower_case_mods: LowerCaseModsRepository, logger: LoggerAdapter):
        self._lower_case_mods = lower_case_mods
        self._logger = logger

    def to_lower(self) -> None:
        self._logger.print_head("Converting uppercase files/folders to lowercase...")
        self._lower_case_mods.to_lower()
