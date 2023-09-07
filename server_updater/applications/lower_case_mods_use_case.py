from server_updater.domain.lower_case_mods_repository import LowerCaseModsRepository


class LowerCaseModsUseCase:
    def __init__(self, lower_case_mods: LowerCaseModsRepository):
        self._lower_case_mods = lower_case_mods

    def to_lower(self) -> None:
        self._lower_case_mods.to_lower()
