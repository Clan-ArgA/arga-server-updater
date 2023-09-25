import os
from dotenv import load_dotenv
import re


load_dotenv()

STEAM_CMD = "/home/steam/steamcmd/steamcmd.sh"
STEAM_USER = os.getenv("STEAM_USER")
STEAM_PASS = os.getenv("STEAM_PASS")

WORKSHOP_CHANGELOG_URL = "https://steamcommunity.com/sharedfiles/filedetails/changelog"
PATTERN = re.compile(r"workshopAnnouncement.*?<p id=\"(\d+)\">", re.DOTALL)

A3_SERVER_ID = "233780"
A3_SERVER_DIR = "/home/steam/steamcmd/arma3"
A3_WORKSHOP_ID = "107410"
A3_WORKSHOP_DIR = f"{A3_SERVER_DIR}/steamapps/workshop/content/{A3_WORKSHOP_ID}"
A3_MODS_DIR = f"{A3_SERVER_DIR}"
A3_MOD_KEYS_SOURCE_DIRECTORY = (
    f"{A3_SERVER_DIR}/steamapps/workshop/content/{A3_WORKSHOP_ID}"
)
A3_MOD_KEYS_DESTINATION_DIRECTORY = f"{A3_SERVER_DIR}/keys"
A3_MODS_LIST_PATH = (
    "/home/steam/scripts/arga-server-updater/server_updater/arma3_mods_list"
)
A3_MOD_DEFAULT = "arga"

REFORGER_SERVER_ID = "1874900"
REFORGER_SERVER_DIR = "/home/steam/steamcmd/reforger"
REFORGER_WORKSHOP_ID = "1874880"
REFORGER_WORKSHOP_DIR = (
    f"{REFORGER_SERVER_DIR}/steamapps/workshop/content/{REFORGER_WORKSHOP_ID}"
)
REFORGER_MODS_DIR = f"{REFORGER_SERVER_DIR}"
REFORGER_ARMA_BINARY = "./ArmaReforgerServer"
REFORGER_CONFIG_FILE = "dynamics_missions.json"
REFORGER_ARMA_MAX_FPS = 60
REFORGER_ARMA_PROFILE = f"{REFORGER_SERVER_DIR}/profile"
REFORGER_ARMA_CONFIG = f"{REFORGER_SERVER_DIR}/config/{REFORGER_CONFIG_FILE}"
REFORGER_ARMA_ARMA_PARAMS = ""
