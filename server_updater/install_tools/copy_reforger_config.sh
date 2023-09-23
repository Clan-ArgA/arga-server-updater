#!/bin/bash

steamcmd_config="/home/steam/steamcmd/reforger/config"

if [ ! -d "$steamcmd_config" ]; then
    mkdir -p "$steamcmd_config"
fi

cp /home/steam/scripts/arga-server-updater/server_updater/reforger_config/*.json /home/steam/steamcmd/reforger/config
