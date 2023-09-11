import os
import shutil

from server_updater.domain.exceptions.decorators.generic_error_handler import (
    generic_error_handler,
)
from server_updater.domain.mods_key_files.mod_sign_key_file_port import (
    ModSignKeyFilePort,
)


class ModSignKeyFileAdapter(ModSignKeyFilePort):
    def __init__(self, source_directory: str, destination_directory: str):
        self._source_directory = source_directory
        self._destination_directory = destination_directory

    @generic_error_handler
    def copy(self) -> str:
        """Copy the Mods sign files."""

        # Find files with the .bikey extension in the source directory
        for root_dir, _, files in os.walk(self._source_directory):
            for file in files:
                if not file.endswith(".bikey"):
                    continue
                source_file_path = os.path.join(root_dir, file)
                destination_file_path = os.path.join(self._destination_directory, file)
                # Copy the file to the destination folder
                shutil.copy(source_file_path, destination_file_path)

        return "Mods sign key files was successfully copied."
