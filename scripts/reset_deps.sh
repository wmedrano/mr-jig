#!/bin/bash

# Assert that the script is running from a Python venv.
if [ -z "$VIRTUAL_ENV" ]; then
    echo "This script must be run from a Python virtual environment."
    exit 1
fi

pip freeze | xargs pip uninstall -y
pip install -r requirements.txt