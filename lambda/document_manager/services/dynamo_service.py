import boto3

dynamodb = boto3.resource('dynamodb')

def store_file_metadata(event):

    try:
        table = dynamodb.Table('document-manager')
        response = table.put_item(
            Item=event["metadata"]
        )
        return response
    except Exception as e:
        print('Error saving metadata to DynamoDB: ', e)