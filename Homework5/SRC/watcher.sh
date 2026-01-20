#!/bin/bash
DIR="/home/$(whoami)/watch"

echo "Watching directory: $DIR"

inotifywait -m -e close_write --format '%w%f' "$DIR" |
while read fullpath; do
    echo "New file detected: $(basename "$fullpath")"
    if [ -f "$fullpath" ]; then
        cat "$fullpath"
        mv "$fullpath" "$fullpath.back"
    else
        echo "Warning: file not found at $fullpath"
    fi
done
