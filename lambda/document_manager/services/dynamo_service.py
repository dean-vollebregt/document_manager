import boto3

def dynamo_service():

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('document-manager')

    response = table.get_item(
        Key={
            'title': 'data'
        })
