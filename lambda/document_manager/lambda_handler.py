import json
import boto3

from services.s3_service import upload_file

def lambda_handler(event, context):

    upload_file(event)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


