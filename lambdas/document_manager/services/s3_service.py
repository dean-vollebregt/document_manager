import json
import base64
import boto3

s3 = boto3.resource('s3', region_name='ap-southeast-2')


def upload_file(event):

    try:
        obj = s3.Object("document-manager-demo", event["fileName"])
        response = obj.put(Body=base64.b64decode(event["fileData"]))
        return response
    except Exception as e:
        print('Error uploading to S3: ', e)


def delete_file(event):

    try:
        response = s3.Object("document-manager-demo", event["fileName"]).delete()
        return response
    except Exception as e:
        print('Error deleting file from S3: ', e)