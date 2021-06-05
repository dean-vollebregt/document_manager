import base64
import boto3


def upload_file(event):

    s3 = boto3.client('s3', region_name='ap-southeast-2')

    try:
        response = s3.put_object(
            Body=base64.b64decode(event["fileData"]),
            Bucket='document-manager-demo',
            Key=event['fileName']
        )
        return response
    except Exception as e:
        print('Error uploading to S3: ', e)


def delete_file(event):

    s3 = boto3.client('s3', region_name='ap-southeast-2')

    try:
        response = s3.delete_object(
            Bucket='document-manager-demo',
            Key=event['fileName'],
        )
        return 0
    except Exception as e:
        print('Error deleting file from S3: ', e)