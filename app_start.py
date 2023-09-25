import argparse
from typing import Dict, Optional

from server_updater.constants import Server
from server_updater.log import Log
from server_updater.main import ServerUpdater
from server_updater.steamcmd import SteamCmd


def run_in_terminal(
    server: Server, option: Optional[str] = None, mods_list_name: Optional[str] = None
) -> None:
    server_updater = ServerUpdater(
        logger=Log(),
        steamcmd=SteamCmd(server=server),
        server=server,
        mods_list_name=mods_list_name,
    )
    if option is not None:
        return run_by_command(option, server_updater)
    server_updater.run()


def run_by_command(option: str, server_updater: ServerUpdater) -> None:
    try:
        server_updater.run_choice(selected=option)
    except KeyError:
        print(f"\n'{option}' is an invalid option.")


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run by command or by menu", add_help=True
    )
    parser.add_argument(
        "--server",
        default="arma3",
        choices=["arma3", "reforger"],
        help="Type of operation to perform",
    )
    parser.add_argument(
        "--mods",
        default="arga",
        help="Specify the mods to update (default: arga)",
    )
    parser.add_argument(
        "--option",
        default=None,
        help="To run an option directly",
    )
    return parser


def get_server_map() -> Dict[str, Server]:
    return {
        "arma3": Server.A3,
        "reforger": Server.REFORGER,
    }


def main() -> None:
    parser = get_parser()
    args = parser.parse_args()
    server = get_server_map()[args.server]
    mods_list = args.mods if server == Server.A3 else None
    run_in_terminal(server=server, option=args.option, mods_list_name=mods_list)


if __name__ == "__main__":
    main()
