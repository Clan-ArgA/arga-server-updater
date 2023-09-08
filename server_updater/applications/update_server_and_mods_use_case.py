from server_updater.applications.update_mods_only_use_case import UpdateModsOnlyUseCase
from server_updater.applications.update_server_only_use_case import (
    UpdateServerOnlyUseCase,
)


class UpdateServerAndModsUseCase:
    def __init__(
        self,
        update_server_only_use_case: UpdateServerOnlyUseCase,
        update_mod_only_use_case: UpdateModsOnlyUseCase,
    ):
        self._update_server_only_use_case = update_server_only_use_case
        self._update_mod_only_use_case = update_mod_only_use_case

    def update(self):
        self._update_server_only_use_case.update()
        self._update_mod_only_use_case.update()
