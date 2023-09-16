#!/bin/bash

cd /home/steam/scripts/
git clone https://VulturARG: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/Clan-ArgA/arga-server-updater.git
cd arga-server-updater
git checkout lb_arma3_plus_reforger
git pull
#echo "STEAM_USER=user" > ./server_updater/.env
#echo "STEAM_PASS=pass" >> ./server_updater/.env
pip install --no-cache-dir -r requirements.txt