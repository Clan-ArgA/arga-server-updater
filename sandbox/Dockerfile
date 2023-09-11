FROM debian:bullseye-slim

LABEL maintainer="Clan ArgA"

RUN apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests \
        git \
        curl \
        python3 \
        nano \
        pip \
        rename \
        lib32stdc++6 \
        lib32gcc-s1 \
        libcurl4 \
        wget \
        ca-certificates && \
    apt-get remove --purge -y && \
    apt-get clean autoclean &&  \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /home/steam && \
    cd /home/steam && \
    mkdir logs

RUN mkdir /home/steam/steamcmd &&  \
    cd /home/steam/steamcmd && \
    curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar zxvf -

RUN mkdir /home/steam/scripts &&  \
    cd /home/steam/scripts \

