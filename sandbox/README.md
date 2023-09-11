```bash
cd /home/steam/scripts/
git clone https://vulturARG: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@github.com/Clan-ArgA/arga-server-updater.git
cd arga-server-updater
git checkout stage-1_refactor_script
echo "STEAM_USER=argasteam" > ./server_updater/.env
echo "STEAM_PASS=wsx147zaqsteam" >> ./server_updater/.env
pip install -r ./server_updater/requirements.txt
python3 app_start.py
```


Descargar server
```bash
./steamcmd.sh +force_install_dir /home/steam/steamcmd/arma3 +login argasteam wsx147zaqsteam +app_update 233780 validate +quit
```

Descargar mod
```bash
./steamcmd.sh +force_install_dir /home/steam/steamcmd/arma3 +login argasteam wsx147zaqsteam +workshop_download_item 107410 1236465508 validate +quit
```


