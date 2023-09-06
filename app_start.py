# MIT License
#
# Copyright (c) 2017 Marcel de Vries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import os.path
import re
import shutil
import time
import sys
import base64


from datetime import datetime
from urllib import request

#region Configuration
STEAM_CMD = "/home/steam/steamcmd/steamcmd.sh"
STEAM_USER = "anonymous"
STEAM_PASS = ""
A3_SERVER_ID = "233780"
A3_SERVER_DIR = "/home/steam/steamcmd/arma3"
A3_WORKSHOP_ID = "107410"

A3_WORKSHOP_DIR = f"{A3_SERVER_DIR}/steamapps/workshop/content/{A3_WORKSHOP_ID}"
A3_MODS_DIR = f"{A3_SERVER_DIR}"

MODS = {
   "@ace": "463939057",
   "@arga": "941818681",
   "@cba_a3": "450814997",
   "@cup_core": "583496184",
   "@cup_cwa": "853743366",
   "@cup_terrains_maps": "583544987",
   "@faa": "533828207",
   "@project_opfor": "735566597",
   "@rhsafrf": "843425103",
   "@rhsgref": "843593391",
   "@rhsusaf": "843577117",
   "@ace_compat_gm": "2633534991",
   "@acre2_global_mobilization_compat": "1740990569",

#ia
   "@vcom": "721359761",
   # "@immerse": "825172265",
   # "@lambs_rpg": "1858070328",
   # "@lambs_turrets": "1862208264",
   # "@lambs_suppression": "1808238502",
   "@lambs_danger": "1858075458",
   "@ia_not_grass": "2946868556",

#mapas
   # "@interiors-cup": "1883956552",
   # "@em_buildings": "671539540",
   # "@anizay": "1537973181",
   # "@beketov": "743968516",
   # "@bozoum": "2618329388",
   # "@deniland": "1231955722",
   # "@hebontes": "1412917989",
   # "@kujari": "1726494027",
   # "@maksniemi": "2696444371",
   # "@mull_of_kintyre": "1982652717",
   # "@ruegen": "835257174",
   # "@saint_kapaulio": "939686262",
   "@tembelan_island": "1252091296",
   "@umb_colombia": "2266710560",
   "@vidda": "1282716647",
   # "@virolahti": "1926513010",
   "@deformer": "2822758266",
   # "@simplecraters": "2853200431",
   # "@improvedcraters": "2886141254",

#medicos
   # "@acex": "708250744",
   # "@ace_legacy": "1963810039",
   # "@ace_cpr":     "1957746437",
   # "@adv_ace_cpr": "1957746437",
   # "@adv_medical": "1353873848",
   "@kat": "2020940806",
   # "@kat_sound": "2447089324",
   # "@kat_air": "2448877245",
   # "@kat_blood": "2441179531",


#malvinas
   # "@cmd2035": "715135712",
   "@flk_ships": "1848941317",
   # "@gcam": "909893746",
   # "@malvinas": "1692037148",
   # "@malvinas_oeste": "1084942536",
   # "@mvl_core": "2014507053",
   "@mlv_units": "2777934829",
   # "@mvl_maps": "2041997442",
   # "@mlv_maps_norocks": "2804685594",
   # "@mvl_maps_west": "1084942536",
   # "@paddle": "887302721",
   # "@proy_1982": "1266670664",
   "@puertoarg": "680323177",

#sonido
    "@acre2": "751965892",
    # "@taskforce": "620019431",
    "@tfar": "894678801",
    # "@achilles": "723217262",
    # "@pike": "1957746437",
    # "@patch": "2010438452",

#cooperativos
    # "@rhssaf": "843632231",
    # "@ace-gref": "884966711",
    # "@ace-united": "773125288",
    # "@ace-armed": "773131200",
    "@blastcore": "2257686620",
    "@clv_core": "2874965023",
    "@clv_airvehicles": "2875337711",
    # "@cvl": "2415601526",
    # "@cvl_armored": "2490539128",
    "@ffaa": "820994401",
    # "@splendid_smoke": "770418577",
    "@task_force_timberwolf_female_characters": "2021778690",
    "@realsim": "2664892656",
    "@uc89": "2732131116",
    "@uss_cva31": "2536035098",

#testeosyextras
    # "@dcg": "764848181",
    # "@niarms-all-in-one":"1208517358",
    # "@niarms-aio-rhs-compat": "1400574293",
    # "@cup-ace3": "1375890861",
    # "@ctab": "871504836",
    # "@frxastfar-extra": "1606874412",
    # "@rm-splinter-gear": "878512695",
    # "@ace-compat-mlo": "1110082605",
    # "@mlo-all-in-one": "823636749",
    # "@em": "333310405",
    # "@extra": "916062070",
    # "@evs": "1223309664",
    # "@shacktac": "498740884",
    # "@hmcs": "952560410",
    # "@op_cos": "1713301206",
    # "@treb": "769440155",
    # "@treb_ace": "1267657613",
    # "@panz": "1236465508"
}

EXTRA_MODS = {
    # 'extdb3': 'extdb3'
}

PATTERN = re.compile(r"workshopAnnouncement.*?<p id=\"(\d+)\">", re.DOTALL)
WORKSHOP_CHANGELOG_URL = "https://steamcommunity.com/sharedfiles/filedetails/changelog"
#endregion

#region Functions
def log(msg):
    print("")
    print("{{0:=<{}}}".format(len(msg)).format(""))
    print(msg);
    print("{{0:=<{}}}".format(len(msg)).format(""))


def call_steamcmd(params):
    os.system("{} {}".format(STEAM_CMD, params))
    print("")


def update_server():
    call_steamcmd(" +force_install_dir {} +quit".format(A3_SERVER_DIR))
    steam_cmd_params  = " +login {} {}".format(STEAM_USER, STEAM_PASS)
#    steam_cmd_params += " +force_install_dir {}".format(A3_SERVER_DIR)
    steam_cmd_params += " +app_update {} validate".format(A3_SERVER_ID)
    steam_cmd_params += " +quit"

    call_steamcmd(steam_cmd_params)


def mod_needs_update(mod_id, path):
    if os.path.isdir(path):
        response = request.urlopen("{}/{}".format(WORKSHOP_CHANGELOG_URL, mod_id)).read()
        response = response.decode("utf-8")
        match = PATTERN.search(response)

        if match:
            updated_at = datetime.fromtimestamp(int(match.group(1)))
            created_at = datetime.fromtimestamp(os.path.getctime(path))

            return (updated_at >= created_at)

    return False


def update_mods():
    for mod_name, mod_id in MODS.items():
        path = "{}/{}".format(A3_WORKSHOP_DIR, mod_id)

        # Check if mod needs to be updated
        if os.path.isdir(path):

            if mod_needs_update(mod_id, path):
                # Delete existing folder so that we can verify whether the
                # download succeeded
                shutil.rmtree(path)
            else:
                print("No update required for \"{}\" ({})... SKIPPING".format(mod_name, mod_id))
                continue
        call_steamcmd(" +force_install_dir {} +quit".format(A3_SERVER_DIR))

        # Keep trying until the download actually succeeded
        tries = 0
        while os.path.isdir(path) == False and tries < 10:
            log("Updating \"{}\" ({}) | {}".format(mod_name, mod_id, tries + 1))
            steam_cmd_params  = " +login {} {}".format(STEAM_USER, STEAM_PASS)
            steam_cmd_params += " +force_install_dir {}".format(A3_SERVER_DIR)
            steam_cmd_params += " +workshop_download_item {} {} validate".format(
                A3_WORKSHOP_ID,
                mod_id
            )
            steam_cmd_params += " +quit"

            call_steamcmd(steam_cmd_params)

            # Sleep for a bit so that we can kill the script if needed
            time.sleep(5)

            tries = tries + 1

        if tries >= 10:
            log("!! Updating {} failed after {} tries !!".format(mod_name, tries))


def lowercase_workshop_dir():
    os.system("(cd {} && find . -depth -exec rename -v 's/(.*)\/([^\/]*)/$1\/\L$2/' {{}} \;)".format(A3_WORKSHOP_DIR))


def create_mod_symlinks():
    for mod_name, mod_id in MODS.items():
        link_path = "{}/{}".format(A3_MODS_DIR, mod_name)
        real_path = "{}/{}".format(A3_WORKSHOP_DIR, mod_id)

        if os.path.isdir(real_path):
            if not os.path.islink(link_path):
                os.symlink(real_path, link_path)
                print("Creating symlink '{}'...".format(link_path))
        else:
            print("Mod '{}' does not exist! ({})".format(mod_name, real_path))
#endregion

def start_server():
    print()
    time.sleep(1)
    print()

    choice = input("""
                      A: Start Update of server and Mods
                      B: Start Update of Mods only
                      C: Start Update of Server only
                      D: Create mod symlinks
                      E: Lower case mods
                      Q: Quit/Log Out
                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        log("Updating A3 server ({})".format(A3_SERVER_ID))
        update_server()
        log("Updating mods")
        update_mods()
        log("Converting uppercase files/folders to lowercase...")
        lowercase_workshop_dir()
        log("Creating symlinks...")
        create_mod_symlinks()
        start_server()
    elif choice == "B" or choice =="b":
        log("Updating mods")
        update_mods()
        log("Converting uppercase files/folders to lowercase...")
        lowercase_workshop_dir()
        log("Creating symlinks...")
        create_mod_symlinks()
        start_server()
    elif choice == "C" or choice =="c":
        log("Updating A3 server ({})".format(A3_SERVER_ID))
        update_server()
        start_server()
    elif choice.lower() == "d":
        create_mod_symlinks()
    elif choice.lower() == "e":
        lowercase_workshop_dir()
    elif choice=="Q" or choice=="q":
        print("Closing Program now")
        sys.exit()
    else:
        print("You must only select either A,B,C,D,E,F or Q to quit.")
        print("Please try again")
        start_server()

start_server()
