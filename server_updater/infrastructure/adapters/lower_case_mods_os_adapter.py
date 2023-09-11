import os

from server_updater.config import A3_WORKSHOP_DIR
from server_updater.domain.exceptions.decorators.generic_error_handler import (
    generic_error_handler,
)
from server_updater.domain.lower_case_mods.lower_case_mods_port import (
    LowerCaseModsPort,
)


class LowerCaseModsOsAdapter(LowerCaseModsPort):
    @generic_error_handler
    def to_lower(self) -> None:
        """Converts the name of each mod to lowercase text."""
        os.system(
            f"(cd {A3_WORKSHOP_DIR} && find . -depth -exec rename -v 's/(.*)\/([^\/]*)/$1\/\L$2/' {{}} \;)"
        )
