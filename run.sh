#!/bin/bash

# This script is intended for development.
# The live site is built and hosted on GitHub pages.

jekyll_version=3.8.6

if (uname | grep -q 'MINGW'); then
    # Using Docker for Windows:
    # Volume path needs extra initial slash!
    volume="/$(pwd)"
    docker="winpty docker"
else
    # Using Linux:
    volume="$(pwd)"
    docker=docker
fi

$docker run --platform linux/amd64 --rm -it --volume=$volume:/srv/jekyll -p 4000:4000 jekyll/jekyll:$jekyll_version\
 jekyll serve --force-polling
