import os
from dotenv import load_dotenv
import re


load_dotenv()

STEAM_CMD = "/home/steam/steamcmd/steamcmd.sh"
STEAM_USER = os.getenv("STEAM_USER")
STEAM_PASS = os.getenv("STEAM_PASS")
A3_SERVER_ID = "233780"
A3_SERVER_DIR = "/home/steam/steamcmd/arma3"
A3_WORKSHOP_ID = "107410"
A3_WORKSHOP_DIR = f"{A3_SERVER_DIR}/steamapps/workshop/content/{A3_WORKSHOP_ID}"
A3_MODS_DIR = f"{A3_SERVER_DIR}"
WORKSHOP_CHANGELOG_URL = "https://steamcommunity.com/sharedfiles/filedetails/changelog"
PATTERN = re.compile(r"workshopAnnouncement.*?<p id=\"(\d+)\">", re.DOTALL)
MOD_KEYS_SOURCE_DIRECTORY = (
    "/home/steam/steamcmd/arma3/steamapps/workshop/content/107410"
)
MOD_KEYS_DESTINATION_DIRECTORY = "/home/steam/steamcmd/arma3/keys"
