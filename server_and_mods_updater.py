from server_updater.infrastructure.adapters.i_o_adapter import IOAdapter
from server_updater.main import ServerManager


def main() -> None:
    server_updater = ServerManager(io_adapter=IOAdapter())
    server_updater.run()


if __name__ == "__main__":
    main()
