#!/bin/bash
# ========================================
# Cvina Command Launcher for Linux/macOS
# ========================================

# Get the directory of this script
CVINA_PATH="$(dirname "$0")/source/cvina"

# Run Python with all passed arguments
python3 "$CVINA_PATH/cvinac.py" "$@"