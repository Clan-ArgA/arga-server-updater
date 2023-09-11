import json
from typing import Dict

from server_updater.config import MOD_JSON_FILE
from server_updater.domain.exceptions.decorators.generic_error_handler import generic_error_handler
from server_updater.domain.exceptions.file_exceptions import FileNotFoundException, JSONDecodeException
from server_updater.domain.mods.mods_repository import ModRepository


class ModJSONAdapter(ModRepository):

    def list_mods_by_steam_id(self) -> Dict[str, str]:
        """List the mods"""
        mods = self._read_json_file(file_name=MOD_JSON_FILE)
        return {key: value["name"] for key, value in mods.items()}

    def save_mods_to_json(self, file_name: str, mods: Dict[str, Dict[str, str]]) -> None:
        """Save the Mods to a JSON file."""
        with open(file_name, 'w') as file:
            json.dump(mods, file, indent=4)

    @generic_error_handler
    def _read_json_file(self, file_name: str) -> Dict[str, Dict[str, str]]:
        try:
            with open(file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundException(file_name)
        except json.JSONDecodeError as e:
            raise JSONDecodeException(f"{e}")

