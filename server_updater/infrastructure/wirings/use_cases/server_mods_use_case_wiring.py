from server_updater.applications.update_server_and_mods_use_case import (
    UpdateServerAndModsUseCase,
)
from server_updater.infrastructure.wirings.use_cases.mod_use_case_wiring import (
    ModUseCaseWiring,
)
from server_updater.infrastructure.wirings.use_cases.server_use_case_wiring import (
    ServerUseCaseWiring,
)


class SeverModsUseCaseWiring:
    @staticmethod
    def instantiate() -> UpdateServerAndModsUseCase:
        return UpdateServerAndModsUseCase(
            update_server_only_use_case=ServerUseCaseWiring().instantiate(),
            update_mod_only_use_case=ModUseCaseWiring().instantiate(),
        )
