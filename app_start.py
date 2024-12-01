from argparse import ArgumentParser, ArgumentTypeError, Namespace

from server_updater.constants import Server
from server_updater.log import Log
from server_updater.main import ServerUpdater
from server_updater.steamcmd import SteamCmd


def select_run_mode(
    server: Server,
    option: str | None = None,
    mods_list_name: str | None = None,
    repair: str | None = None,
) -> None:
    server_updater = ServerUpdater(
        logger=Log(),
        steamcmd=SteamCmd(server=server),
        server=server,
        mods_list_name=mods_list_name,
        repair=repair,
    )
    if repair is not None:
        return server_updater.repair_arma3_mod()
    if option is not None:
        return run_by_command(option, server_updater)
    server_updater.run()


def run_by_command(option: str, server_updater: ServerUpdater) -> None:
    try:
        server_updater.run_choice(selected=option)
    except KeyError:
        print(f"\n'{option}' is an invalid option.")


def get_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Run by command or by menu", add_help=True)
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
        nargs="+",
        default=None,
        help="To run an option directly",
    )
    parser.add_argument(
        "--repair",
        help="Reinstall the specified mod.",
    )
    return parser


def get_server_map() -> dict[str, Server]:
    return {
        "arma3": Server.A3,
        "reforger": Server.REFORGER,
    }


def sanitize_option(args: Namespace) -> Namespace:
    if len(args.option) > 1:
        raise ArgumentTypeError(f"'{args.option}' is an invalid option.")

    args.option = args.option[0]
    return args


def parser_option(args: Namespace) -> Namespace:
    options = args.option
    if not options:
        return args

    options_set = {opt.lower() for opt in options}
    if "server" in options_set and any(opt in options_set for opt in {"mods", "mod"}):
        args.option = "a"
        return args

    if "server" in options_set:
        args.option = "c"
        return args

    if any(opt in options_set for opt in {"mods", "mod"}):
        args.option = "b"
        return args

    return sanitize_option(args)


def main() -> None:
    parser = get_parser()
    args = parser.parse_args()
    args = parser_option(args)
    server = get_server_map()[args.server]
    mods_list = args.mods if server == Server.A3 else None
    select_run_mode(
        server=server, option=args.option, mods_list_name=mods_list, repair=args.repair
    )


if __name__ == "__main__":
    main()
