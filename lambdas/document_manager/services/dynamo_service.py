import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('document-manager')

def store_file_metadata(event):

    try:
        response = table.put_item(
            Item=event["metadata"]
        )
        return response
    except Exception as e:
        print('Error saving metadata to DynamoDB: ', e)


def read_file_metadata():

    try:
        response = table.scan()
        return response["Items"]
    except Exception as e:
        print('Error reading metadata from DynamoDB: ', e)


def delete_file_metadata(event):
    try:
        response = table.delete_item(
            Key={
                'title': event["title"]
            }
        )
        return response
    except Exception as e:
        print('Error deleting metadata from DynamoDB: ', e)