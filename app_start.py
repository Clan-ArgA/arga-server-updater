from server_updater.infrastructure.adapters.logger_adapter import LoggerAdapter
from server_updater.infrastructure.wirings.steamcmd_wiring import SteamcmdWiring
from server_updater.main import ServerUpdater


def main() -> None:
    wiring = SteamcmdWiring()
    server_updater = ServerUpdater(
        logger=LoggerAdapter(), steamcmd=wiring.instantiate()
    )
    server_updater.run()


if __name__ == "__main__":
    main()
