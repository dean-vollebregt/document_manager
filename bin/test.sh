#!/bin/bash
set -euxo pipefail

# Set state so tests can run independently
aws s3 sync ./tests/supporting s3://document-manager-demo
aws dynamodb put-item --table-name document-manager   --item '{"title": {"S": "test_entry"}}'

# Run tests
python3.8 -m unittest discover -s tests/unit/* -p "*_test.py"