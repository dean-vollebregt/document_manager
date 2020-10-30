#!/bin/bash
set -euxo pipefail

function build_document_manager() {
    cd lambdas/document_manager
    python3.8 -m venv v-env && source v-env/bin/activate
    pip3.8 install -r requirements.txt -t ./
    zip -r documentManager.zip * -x "v-env*" -x "*.dist-info*"
    aws s3 sync . s3://document-manager-demo --acl private --exclude "*" --include "documentManager.zip"
    rm -rf documentManager.zip
    deactivate
}

build_document_manager