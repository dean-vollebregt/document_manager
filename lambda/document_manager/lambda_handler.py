from services.s3_service import upload_file, delete_file
from services.dynamo_service import store_file_metadata, read_file_metadata, delete_file_metadata


def lambda_handler(event, context):

    if event["operation"] == "upload_file":
        return upload_file(event)
    elif event["operation"] == "delete_file":
        return delete_file(event)
    elif event["operation"] == "store_file_metadata":
        return store_file_metadata(event)
    elif event["operation"] == "read_file_metadata":
        return read_file_metadata()
    elif event["operation"] == "delete_file_metadata":
        return delete_file_metadata(event)
    else:
        print("Operation not found")