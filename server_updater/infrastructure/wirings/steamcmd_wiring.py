from server_updater.config import STEAM_USER, STEAM_PASS
from server_updater.infrastructure.adapters.steamcmd_adapter import SteamCmd


class SteamcmdWiring:
    @staticmethod
    def instantiate() -> SteamCmd:
        return SteamCmd(steam_user=STEAM_USER, steam_pass=STEAM_PASS)
