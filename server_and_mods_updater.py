import argparse
from typing import Dict, Any

import uvicorn

from server_updater.infrastructure.adapters.i_o_terminal_adapter import IOTerminalAdapter
from server_updater.infrastructure.fastapi.endpoints.endpoints import app
from server_updater.main import ServerManager


def run_in_terminal() -> None:
    server_updater = ServerManager(io_adapter=IOTerminalAdapter())
    server_updater.run()


def run_fastapi_server() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run a command or FastAPI server", add_help=True
    )
    parser.add_argument(
        "--type",
        default="command",
        choices=["command", "fastapi"],
        help="Type of operation to perform",
    )

    return parser


def get_type_map() -> Dict[str, Any]:
    return {
        "command": run_in_terminal,
        "fastapi": run_fastapi_server,
    }


def main() -> None:
    parser = get_parser()
    type_map = get_type_map()
    type_map.get(parser.parse_args().type)()


if __name__ == "__main__":
    main()
