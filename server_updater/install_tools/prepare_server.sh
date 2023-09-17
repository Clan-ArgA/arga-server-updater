#!/bin/bash

apt-get update
apt-get install -y --no-install-recommends --no-install-suggests \
    curl \
    python3 \
    nano \
    pip \
    rename \
    lib32stdc++6 \
    lib32gcc-s1 \
    libcurl4 \
    wget \
    ca-certificates
apt-get remove --purge -y
apt-get clean autoclean
apt-get autoremove -y
rm -rf /var/lib/apt/lists/*

steam_home="/home/steam"
steamcmd_dir="$steam_home/steamcmd"

if [ ! -d "$steam_home" ]; then
    mkdir -p "$steam_home"
fi
if [ ! -d "$steamcmd_dir" ]; then
    mkdir -p "$steamcmd_dir"
fi
cd /home/steam/steamcmd
curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar zxvf -

cd /home/steam/scripts/arga-server-updater
echo "STEAM_USER=anonymous" > ./server_updater/.env
echo "STEAM_PASS=" >> ./server_updater/.env

cp /home/steam/scripts/arga-server-updater/server_updater/reforger_server_config.json /home/steam/steamcmd/reforger/config