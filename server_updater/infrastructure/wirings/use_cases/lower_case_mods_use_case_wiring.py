from server_updater.applications.lower_case_mods_use_case import LowerCaseModsUseCase
from server_updater.infrastructure.adapters.logger_adapter import LoggerAdapter
from server_updater.infrastructure.adapters.lower_case_mods_adapter import LowerCaseModsAdapter


class LowerCaseModsUseCaseWiring:
    @staticmethod
    def instantiate() -> LowerCaseModsUseCase:
        return LowerCaseModsUseCase(
            lower_case_mods=LowerCaseModsAdapter(),
            logger=LoggerAdapter(),
        )

