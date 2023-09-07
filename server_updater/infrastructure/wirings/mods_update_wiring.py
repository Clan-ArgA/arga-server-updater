from server_updater.config import WORKSHOP_CHANGELOG_URL, A3_WORKSHOP_DIR
from server_updater.infrastructure.adapters.i_o_adapter import IOAdapter
from server_updater.infrastructure.adapters.logger_adapter import LoggerAdapter
from server_updater.infrastructure.adapters.mods_adapter import ModAdapter
from server_updater.infrastructure.adapters.mods_update_adapter import ModsUpdateAdapter
from server_updater.infrastructure.adapters.steamcmd_adapter import SteamCmd
from server_updater.infrastructure.wirings.steamcmd_wiring import SteamcmdWiring


class ModUpdateWiring:
    def instantiate(self) -> ModsUpdateAdapter:
        return ModsUpdateAdapter(
            logger=LoggerAdapter(),
            steamcmd=self._steamcmd(),
            mods=ModAdapter(),
            input_output=IOAdapter(),
            a3_workshop_dir=A3_WORKSHOP_DIR,
            workshop_changelog_url=WORKSHOP_CHANGELOG_URL,
        )

    @staticmethod
    def _steamcmd() -> SteamCmd:
        wiring = SteamcmdWiring()
        return wiring.instantiate()
