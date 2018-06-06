#!/bin/bash

# This script is intended for development only!
# In a production environment use:
#      docker-compose up -d

version=$(cat docker-compose.yml | grep -oP '(?<=jekyll/jekyll:)[0-9.]+$')

if (uname | grep -q 'MINGW'); then
    # Using Docker for Windows:
    # Volume path needs extra initial slash!
    volume="/$(pwd)/blog"
    docker="winpty docker"
else
    # Using Linux:
    volume="$(pwd)/blog"
    docker=docker
fi

$docker run --rm -it --volume=$volume:/srv/jekyll -p 4000:4000 jekyll/jekyll:$version jekyll serve --force-polling
