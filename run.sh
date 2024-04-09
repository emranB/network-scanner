#!/bin/bash

# Get root path if not provided
if [ -z "$1" ]; then
    ROOT_PATH=$(dirname "$(realpath "$0")")
    echo "Root path: $ROOT_PATH"
else
    ROOT_PATH="$1"
fi

# Check if main.py exists
if [ ! -f "$ROOT_PATH/networkscanner/main.py" ]; then
    echo "Error: $ROOT_PATH/networkscanner/main.py not found. Exitting. . . ."
    exit 1
fi
# Check if config.json exists
if [ ! -f "$ROOT_PATH/networkscanner/config.json" ]; then
    echo "Error: $ROOT_PATH/networkscanner/config.py not found. Exitting. . . ."
    exit 1
fi

# Run main.py script with Poetry
poetry run python "$ROOT_PATH/networkscanner/main.py" "$ROOT_PATH"