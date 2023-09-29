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

steamcmd_dir="/home/steam/steamcmd"

if [ ! -d "$steamcmd_dir" ]; then
    mkdir -p "$steamcmd_dir"
fi
cd /home/steam/steamcmd
curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar zxvf -

echo "STEAM_USER=anonymous" > /home/steam/scripts/arga-server-updater/server_updater/.env
echo "STEAM_PASS=" > /home/steam/scripts/arga-server-updater/server_updater/.env

