from server_updater.config import WORKSHOP_CHANGELOG_URL, A3_WORKSHOP_DIR
from server_updater.infrastructure.adapters.i_o_terminal_adapter import IOTerminalAdapter
from server_updater.infrastructure.adapters.logger_terminal_adapter import LoggerTerminalAdapter
from server_updater.infrastructure.adapters.mods_adapter import ConstanModAdapter
from server_updater.infrastructure.adapters.mods_update_adapter import ModsUpdateAdapter
from server_updater.infrastructure.adapters.steamcmd_adapter import SteamCmd
from server_updater.infrastructure.wirings.steamcmd_wiring import SteamcmdWiring


class ModUpdateWiring:
    def instantiate(self) -> ModsUpdateAdapter:
        return ModsUpdateAdapter(
            logger=LoggerTerminalAdapter(),
            steamcmd=self._steamcmd(),
            mods_repository=ConstanModAdapter(),
            a3_workshop_dir=A3_WORKSHOP_DIR,
            workshop_changelog_url=WORKSHOP_CHANGELOG_URL,
        )

    @staticmethod
    def _steamcmd() -> SteamCmd:
        wiring = SteamcmdWiring()
        return wiring.instantiate()
