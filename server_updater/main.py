import sys
from typing import Dict, Any

from server_updater.domain.miscellaneous.i_o_port import IOPort
from server_updater.infrastructure.wirings.use_cases.create_symlink_use_case_wiring import (
    CreateSymlinkUseCaseWiring,
)
from server_updater.infrastructure.wirings.use_cases.lower_case_mods_use_case_wiring import (
    LowerCaseModsUseCaseWiring,
)
from server_updater.infrastructure.wirings.use_cases.mod_sign_key_file_use_case_wiring import (
    ModSignKeyFileUseCaseWiring,
)
from server_updater.infrastructure.wirings.use_cases.mod_use_case_wiring import (
    ModUseCaseWiring,
)
from server_updater.infrastructure.wirings.use_cases.server_mods_use_case_wiring import (
    SeverModsUseCaseWiring,
)
from server_updater.infrastructure.wirings.use_cases.server_use_case_wiring import (
    ServerUseCaseWiring,
)


class ServerManager:
    def __init__(self, io_adapter: IOPort):
        self._io_adapter = io_adapter

    def run(self):
        choices = self._get_choices()
        while True:
            selected = self._show_options()
            if selected.lower() == "q":
                self._quit()
            try:
                instance = choices.get(selected.lower())().instantiate()
                instance.update()
            except (KeyError, TypeError):
                self._bad_choice()

    def _show_options(self) -> str:
        return self._io_adapter.input()

    def _get_choices(self) -> Dict[str, Any]:
        return {
            "a": SeverModsUseCaseWiring,
            "b": ModUseCaseWiring,
            "c": ServerUseCaseWiring,
            "d": CreateSymlinkUseCaseWiring,
            "e": LowerCaseModsUseCaseWiring,
            "f": ModSignKeyFileUseCaseWiring,
            "q": self._quit,
        }

    def _quit(self) -> None:
        self._io_adapter.output("Closing Program now\n")
        sys.exit()

    def _bad_choice(self) -> None:
        self._io_adapter.output(
            "\nYou must only select either A,B,C,D,E,F or Q to quit."
        )
        self._io_adapter.output("Please try again")
