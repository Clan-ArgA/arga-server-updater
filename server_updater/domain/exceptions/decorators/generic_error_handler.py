import logging

from server_updater.domain.exceptions.base_exceptions import (
    UpdaterWarning,
    UpdaterGenericError,
    UpdaterException,
)

logger = logging.getLogger(__name__)


def generic_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            class_name = args[0].__class__.__name__
        except IndexError:
            class_name = "No class name"
        method_name = func.__name__
        try:
            return func(*args, **kwargs)
        except UpdaterWarning as exc:
            print(f"WARNING: {exc}")
        except UpdaterException as exc:
            logger.error(
                "ERROR: '%s' exception was raised in the '%s' method of the '%s' class.",
                exc.__class__.__name__,
                method_name,
                class_name,
            )
            logger.error("ERROR MESSAGE: %s", exc)
            print(f"ERROR: {exc}")
        except Exception as exc:
            logger.error(
                "ERROR: '%s' exception was raised in the '%s' method of the '%s' class.",
                exc.__class__.__name__,
                method_name,
                class_name,
            )
            logger.error("ERROR TYPE: %s.", type(exc))
            logger.error("ERROR RAW: %s", exc)
            raise UpdaterGenericError(exc) from exc

    return wrapper
