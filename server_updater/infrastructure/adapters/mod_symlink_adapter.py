import os
from typing import Optional

from server_updater.domain.mod_symlink.mod_symlink_repository import (
    ModSymlinkRepository,
)


class ModSymlinkAdapter(ModSymlinkRepository):
    def __init__(
        self,
        a3_workshop_dir: str,
        workshop_changelog_url: str,
    ):
        self._a3_workshop_dir = a3_workshop_dir
        self._workshop_changelog_url = workshop_changelog_url

    def create(self, mod_name: str, mod_id: str) -> Optional[str]:
        """Create Mod Symlink."""
        link_path = f"{self._a3_workshop_dir}/{mod_name}"
        real_path = f"{self._workshop_changelog_url}/{mod_id}"

        if not os.path.isdir(real_path):
            return f"Mod '{mod_name}' does not exist! ({real_path})"
        if os.path.islink(link_path):
            return None
        os.symlink(real_path, link_path)
        return f"Creating symlink '{link_path}'..."
