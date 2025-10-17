#!/bin/bash
while true; do
    rsync -avz --delete ~/project/ /storage/emulated/0/termux/cloud/
    inotifywait -r -e modify,create,delete ~/project/
done
