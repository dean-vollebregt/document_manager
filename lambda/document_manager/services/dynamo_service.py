import boto3


def store_file_metadata(event):

    dynamodb = boto3.client('dynamodb', region_name='ap-southeast-2')

    try:
        response = dynamodb.put_item(
            TableName='document-manager',
            Item={
                'title': {'S': event['metadata']['title']}
            },
            ReturnValues='ALL_OLD'
        )
        return response['ResponseMetadata']['HTTPStatusCode']

    except Exception as e:
        print('Error saving metadata to DynamoDB: ', e)


def read_file_metadata():

    dynamodb = boto3.client('dynamodb', region_name='ap-southeast-2')

    try:
        response = dynamodb.scan(
            TableName='document-manager',
        )
        return response["Items"]
    except Exception as e:
        print('Error reading metadata from DynamoDB: ', e)


def delete_file_metadata(event):

    dynamodb = boto3.client('dynamodb', region_name='ap-southeast-2')

    try:
        response = dynamodb.delete_item(
            TableName='document-manager',
            Key={
                'title': {'S': event['metadata']['title']}
            },
            ReturnValues='ALL_OLD'
        )
        return response['ResponseMetadata']['HTTPStatusCode']
    except Exception as e:
        print('Error reading metadata from DynamoDB: ', e)