import json
import boto3

from services.s3_service import upload_file
from services.dynamo_service import store_file_metadata

def lambda_handler(event, context):

    if event["operation"] == "create_s3_object":
        upload_file(event)
    elif event["operation"] == "set_meta_data":
        store_file_metadata(event)
    elif event["operation"] == "delete_s3_object":
        return 0
    else:
        print("Operation not found")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }