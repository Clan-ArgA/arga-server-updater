from server_updater.domain.constants import UpdateType
from server_updater.domain.exceptions.base_exceptions import UpdaterException


class SteamcmdException(UpdaterException):
    """Base class for all exceptions in this module."""


class UpdateTypeException(SteamcmdException):
    MESSAGE = ": update_type name is incorrect."

    def __init__(self, update_type: UpdateType):
        self._update_type = update_type.value

    def __str__(self) -> str:
        return f"{self._update_type}{self.MESSAGE}"
