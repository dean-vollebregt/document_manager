import json
import boto3


dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):

    table = dynamodb.Table('document-manager')

    response = table.get_item(
        Key={
            'title': 'data'
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


