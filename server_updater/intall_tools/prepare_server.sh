#!/bin/bash

apt-get update && \
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