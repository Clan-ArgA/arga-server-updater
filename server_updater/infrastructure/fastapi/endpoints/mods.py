from typing import Dict

from pydantic import BaseModel


class Mods(BaseModel):
    mods: Dict[str, Dict[str, str]]
