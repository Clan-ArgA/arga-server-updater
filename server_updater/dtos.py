from dataclasses import dataclass
from typing import Optional


@dataclass
class ServerConfig:
    server_dir: Optional[str] = None
    server_id: Optional[str] = None
    workshop_dir: Optional[str] = None
    workshop_id: Optional[str] = None
    mods_dir: Optional[str] = None
