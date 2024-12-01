# ArgA Server Updater

----
## Arma 3
### To run updater
```bash
sudo -iu steam
cd /home/steam/scripts/arga-server-updater
python3 app_start.py
```

### To run an option from updater
```bash
sudo -iu steam
cd /home/steam/scripts/arga-server-updater
python3 app_start.py --option option
```
Options:
- A: Update server and Mods
- B: Update Mods only
- C: Update Server only

IMPORTANT: When executing the menus referring to MODs, 
only the file that is defined in the A3_MOD_DEFAULT constant of the `config.py` file is processed.

To install or update another list of MODs you must use the following command:
```bash
python3 app_start.py --option b --mod [MOD_LIST_JSON_FILE]
```

The `MOD_LIST_JSON_FILE` file name must be placed without the .json extension. 
The file must have been previously created.

### Force installation of a mod.

Install a mod defined in the default list of `config.py`:
```bash
sudo -iu steam
cd /home/steam/scripts/arga-server-updater
python3 app_start.py --repair mod_name
```

Install a mod defined in any MODs list:
```bash
sudo -iu steam
cd /home/steam/scripts/arga-server-updater
python3 app_start.py --repair mod_name --mod xxxx
```
`mod_name` is the name of the MOD to be reinstalled, as written in the corresponding mod list.
The `xxxx` file name must be placed without the .json extension.

----
## Reforger
### To run updater
```bash
sudo -iu steam
cd /home/steam/scripts/arga-server-updater
python3 app_start.py --server reforger
```

### To run an option from updater
```bash
sudo -iu steam
cd /home/steam/scripts/arga-server-updater
python3 app_start.py --server reforger --option option
```
Options:
- A: Update Server and run Reforger
- B: Run Reforger server
- C: Update Server only

Example: run reforger server from console
```text
python3 app_start.py --server reforger --option b
```

----
## Install
If there is a steam user
```bash
sudo -iu steam
```
```bash
apt-get update && apt-get install -y --no-install-recommends --no-install-suggests git nano python3 pip
mkdir -p /home/steam/scripts
cd /home/steam/scripts
git clone https://github.com/Clan-ArgA/arga-server-updater.git
cd arga-server-updater
pip install --no-cache-dir -r requirements.txt
```

In the case of this error, when using git clone:
```text
fatal: unable to access 'https://github.com/Clan-ArgA/arga-server-updater.git/': server certificate verification failed. CAfile: none CRLfile: none
```
run this command: `apt-get install --reinstall ca-certificates`

Replace the steam username and password in the prepare_server.sh file
```bash
nano /home/steam/scripts/arga-server-updater/server_updater/install_tools/prepare_server.sh
```

Prepare the server
```bash
bash /home/steam/scripts/arga-server-updater/server_updater/install_tools/prepare_server.sh
```

----
## Install Arma 3 Servers and MODs
Create at least one file with the list of MODs that will be used on the server. 
The file name must be xxxx.json. There must exist a file with the name xxxx defined in A3_MOD_DEFAULT.
```bash
nano /home/steam/scripts/arga-server-updater/server_updater/arma3_mods_list/xxxx.json
```
Format:
```json
{
    "@mod_name": "mod_workshop_id",
    "@mod_name_2": "mod_workshop_id_2"
}
```
Names must be lowercase preceded by @.
The last line should not have a comma at the end.


Install server and default list MODs.
```bash
python3 /home/steam/scripts/arga-server-updater/app_start.py --option a
```

Install a specific list MODs only.
```bash
python3 /home/steam/scripts/arga-server-updater/app_start.py --option b --mods xxxx
```

----
To kill Arma 3
```bash
pkill -f "arma"
```

----
## Install Reforger
Configure the reforger server
```bash
nano /home/steam/scripts/arga-server-updater/server_updater/reforger_server_config.json
```

Install the server
```bash
python3 /home/steam/scripts/arga-server-updater/app_start.py --server reforger --option c
```

Copy the reforger server config
```bash
bash /home/steam/scripts/arga-server-updater/server_updater/install_tools/copy_reforger_config.sh
```

----
To kill Arma Reforger
```bash
pkill -f "reforger"
```

----
## Run coverage

```bash
py -m coverage run -m unittest discover
py -m coverage html
```
