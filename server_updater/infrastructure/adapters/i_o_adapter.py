from server_updater.domain.i_o_repository import IORepository


class IOAdapter(IORepository):
    @staticmethod
    def input() -> str:
        """User input."""
        return input(
            """
                      A: Update server and Mods
                      B: Update Mods only
                      C: Update Server only
                      D: Create mod symlinks
                      E: Lower case mods
                      Q: Quit/Log Out
                      Please enter your choice: """
        )

    @staticmethod
    def output(msg: str) -> None:
        """Print the message."""
        print(msg)