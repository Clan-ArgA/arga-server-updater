# arga-server-updater

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
- D: Create mod symlinks
- E: Lower case mods
- F: Copy key files

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

----
## Install
If there is a steam user
```bash
sudo -iu steam
```
```bash
apt-get update
apt-get install -y --no-install-recommends --no-install-suggests git nano
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
cd /home/steam/scripts/arga-server-updater/server_updater/install_tools
nano prepare_server.sh
```

Configure the reforger server
```bash
cd /home/steam/scripts/arga-server-updater
nano reforger_server_config.json
```

Prepare the server
```bash
bash prepare_server.sh
```

