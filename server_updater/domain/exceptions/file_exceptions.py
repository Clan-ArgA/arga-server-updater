from server_updater.domain.exceptions.base_exceptions import UpdaterException


class FileException(UpdaterException):
    """Base class for all exceptions in this module."""


class FileNotFoundException(FileException):
    MESSAGE = "The file"

    def __init__(self, file_name: str):
        self._file_name = file_name

    def __str__(self) -> str:
        return f"{self.MESSAGE} '{self._file_name}' was not found"


class JSONDecodeException(FileException):
    MESSAGE = "Error decoding the JSON file:"

    def __init__(self, file_name: str):
        self._file_name = file_name

    def __str__(self) -> str:
        return f"{self.MESSAGE}: {self._file_name}"
