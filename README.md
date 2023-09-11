# arga-server-updater

### To run
```bash
sudo -iu steam
cd /home/steam/scripts/arga-server-updater
python3 server_and_mods_updater.py --type=xxxx
```
xxxx puede ser `command` o `fastapi`. 

Si no se pone `--type` se toma el valor de `command` por defecto

### To run server sandbox
```bash
cd ./sandbox
docker-compose run --rm arma3 bash
```

Se abre la consola del servidor de pruebas. En la misma hay que clonar el repositorio, de acuerdo a las siguientes instrucciones: 

```bash
cd /home/steam/scripts/
git clone https://user:token@github.com/Clan-ArgA/arga-server-updater.git
cd arga-server-updater
git checkout Stage_3_command_and_fastapi/sandbox
echo "STEAM_USER=steam_user" > ./server_updater/.env
echo "STEAM_PASS=steam_pass" >> ./server_updater/.env
pip install -r ./server_updater/requirements.txt
python3 server_and_mods_updater.py
```

### Ejemplo de descargas manuales

Descargar server
```bash
./steamcmd.sh +force_install_dir /home/steam/steamcmd/arma3 +login argasteam wsx147zaqsteam +app_update 233780 validate +quit
```

Descargar mod
```bash
./steamcmd.sh +force_install_dir /home/steam/steamcmd/arma3 +login argasteam wsx147zaqsteam +workshop_download_item 107410 1236465508 validate +quit
```


