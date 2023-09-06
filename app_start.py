from server_updater.log import Log
from server_updater.main import ServerUpdater
from server_updater.steamcmd import SteamCmd


def main() -> None:
    server_updater = ServerUpdater(logger=Log(), steamcmd=SteamCmd())
    server_updater.run()


if __name__ == "__main__":
    main()
