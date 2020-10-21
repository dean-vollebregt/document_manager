import boto3

s3 = boto3.client('s3',  region_name='ap-southeast-2')

def upload_image():

    try:
        s3.upload_file(
            Filename="./test.txt",
            Bucket="document-manager-demo",
            Key="images/test.txt")
    except Exception as e:
        print('Error uploading to S3: ', e)