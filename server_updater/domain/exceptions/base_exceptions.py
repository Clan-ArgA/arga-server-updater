import logging
from typing import Optional, Any

logger = logging.getLogger(__name__)


class UpdaterException(Exception):
    """Base class for all own exceptions."""

    MESSAGE: Optional[str] = None

    def dict(self) -> dict[str, str]:
        """Return error message as dict"""

        return {"error": f"{self._get_message()}"}

    def _get_message(self) -> str:
        default_message = f"The '{self.__class__.__name__}' base class should not be used to raise exceptions."
        return self.MESSAGE if self.MESSAGE is not None else default_message

    def __str__(self) -> str:
        return self._get_message()


class UpdaterFlGenericError(UpdaterException):
    MESSAGE = ""

    def __init__(
        self,
        exception_or_message: Any,
    ) -> None:
        super().__init__()

        msg = (
            type(exception_or_message)
            if isinstance(exception_or_message, Exception)
            and not isinstance(exception_or_message, UpdaterException)
            else exception_or_message
        )
        self._exception_or_message = msg
        logger.error(f"ERROR: Generic error: {self._exception_or_message}.")

    def dict(self):
        return {"error": f"Generic error: {self._exception_or_message}."}


class UpdaterFlWarning(UpdaterException):
    """Base class for all own warnings."""
