#!/bin/bash
set -euxo pipefail

# Run tests
python3.8 -m pytest -v -s ./test
