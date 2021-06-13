import boto3
import unittest

from botocore.stub import Stubber
from unittest.mock import patch


class StoreFileMetadataTestCase(unittest.TestCase):

    def setUp(self):

        self.dynamo_client = boto3.client('dynamodb', region_name="ap-southeast-2")

        self.dynamo_client_stub = Stubber(self.dynamo_client)

        self.event = {"operation": "store_file_metadata", "metadata": {"title": "test"}}

        self.expected_dynamo_client_params = {
            'TableName': 'document-manager',
            'Item': {
                'title': {'S': 'test'}
            },
            'ReturnValues': 'ALL_OLD'
        }

        self.mocked_response = {
            'ResponseMetadata':
                {
                    'HTTPStatusCode': 200
                }
        }

        self.dynamo_client_stub.add_response('put_item', self.mocked_response, self.expected_dynamo_client_params)
        self.dynamo_client_stub.activate()

    def testInsertFileMetadataSuccessful(self):
        with patch('services.dynamo_service.boto3.client', return_value=self.dynamo_client):
            from services.dynamo_service import store_file_metadata
            result = store_file_metadata(self.event)
            assert result == 200, "DynamoDB should persist the metadata to the document-manger table"


class ReadFileMetadataTestCase(unittest.TestCase):

    def setUp(self):

        self.dynamo_client = boto3.client('dynamodb', region_name="ap-southeast-2")

        self.dynamo_client_stub = Stubber(self.dynamo_client)

        self.event = {"operation": "read_file_metadata"}

        self.expected_dynamo_client_params = {
            'TableName': 'document-manager',
        }

        self.mocked_response = {
           "Items":[
              {
                 "fileName":{"S":"screenshot.png"},
                 "description":{"S":"screenshot"},
                 "date_created":{"S":"28/10/2020"},
                 "reference":{"S":"https://document-manager-demo.s3-ap-southeast-2.amazonaws.com/screenshot.png"},
                 "title":{"S":"screenshot"}
              }
           ],
           "ResponseMetadata":{
              "HTTPStatusCode":200
           }
        }

        self.dynamo_client_stub.add_response('scan', self.mocked_response, self.expected_dynamo_client_params)
        self.dynamo_client_stub.activate()

    def testReadFileMetadataSuccessful(self):
        with patch('services.dynamo_service.boto3.client', return_value=self.dynamo_client):
            from services.dynamo_service import read_file_metadata
            result = read_file_metadata()
            assert result[0]['fileName']['S'] == "screenshot.png", "DynamoDB should scan the document-manger table"


class DeleteFileMetadataTestCase(unittest.TestCase):

    def setUp(self):

        self.dynamo_client = boto3.client('dynamodb', region_name="ap-southeast-2")

        self.dynamo_client_stub = Stubber(self.dynamo_client)

        self.event = {"operation": "store_file_metadata", "metadata": {"title": "test"}}

        self.expected_dynamo_client_params = {
            'TableName': 'document-manager',
            'Key': {
                'title': {'S': 'test'}
            },
            'ReturnValues': 'ALL_OLD'
        }

        self.mocked_response = {
           "ResponseMetadata":{
              "HTTPStatusCode": 200
           }
        }

        self.dynamo_client_stub.add_response('delete_item', self.mocked_response, self.expected_dynamo_client_params)
        self.dynamo_client_stub.activate()

    def testDeleteFileMetadataSuccessful(self):
        with patch('services.dynamo_service.boto3.client', return_value=self.dynamo_client):
            from services.dynamo_service import delete_file_metadata
            result = delete_file_metadata(self.event)
            assert result == 200, "DynamoDB should delete the file metadata from the document-manger table"