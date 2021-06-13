#!/bin/bash
set -euxo pipefail

function deploy_document_manager() {
    aws lambda update-function-code --function-name documentManager --s3-bucket document-manager-demo --s3-key documentManager.zip
}

function update_cloudformation_stack() {
    cd cloudformation
    aws s3 sync . s3://document-manager-demo --exclude "*" --include "document_manager.yml"
    aws cloudformation update-stack --stack-name documentmanager \
    --template-url 'https://document-manager-demo.s3-ap-southeast-2.amazonaws.com/document_manager.yml' --capabilities CAPABILITY_NAMED_IAM
}

function sync_public_assets() {
    cd ../public
    aws s3 sync . s3://document-manager-demo
}

function main(){
  deploy_document_manager
  update_cloudformation_stack
  sync_public_assets
}

main