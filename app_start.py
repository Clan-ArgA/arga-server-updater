import argparse
from typing import Dict, Any

from server_updater.constants import Server
from server_updater.log import Log
from server_updater.main import ServerUpdater
from server_updater.steamcmd import SteamCmd


def run_in_terminal(server: Server) -> None:
    server_updater = ServerUpdater(
        logger=Log(), steamcmd=SteamCmd(server=server), server=server
    )
    server_updater.run()


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run a command or FastAPI server", add_help=True
    )
    parser.add_argument(
        "--server",
        default="arma3",
        choices=["arma3", "reforger"],
        help="Type of operation to perform",
    )
    return parser


def get_server_map() -> Dict[str, Server]:
    return {
        "arma3": Server.A3,
        "reforger": Server.REFORGER,
    }


def main() -> None:
    parser = get_parser()
    server = get_server_map()[parser.parse_args().server]
    run_in_terminal(server=server)


if __name__ == "__main__":
    main()
