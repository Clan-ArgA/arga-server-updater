from server_updater.config import WORKSHOP_CHANGELOG_URL, A3_WORKSHOP_DIR
from server_updater.infrastructure.adapters.mod_symlink_adapter import ModSymlinkAdapter


class ModSymlinkWiring:
    @staticmethod
    def instantiate() -> ModSymlinkAdapter:
        return ModSymlinkAdapter(
            a3_workshop_dir=A3_WORKSHOP_DIR,
            workshop_changelog_url=WORKSHOP_CHANGELOG_URL,
        )
