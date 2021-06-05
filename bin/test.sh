#!/bin/bash
set -euxo pipefail

# Run tests
python3.8 -m unittest discover -s tests/unit/* -p "*_test.py"