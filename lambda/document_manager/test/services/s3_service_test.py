import boto3
import unittest

from unittest.mock import Mock, patch
from services.s3_service import upload_file, delete_file


class TestS3Services(unittest.TestCase):

    def setUp(self):
        self.s3_client = Mock()

    def test_upload_file(self):
        with patch.object(boto3, 'client', return_value=self.s3_client):
            self.event = {"operation": "createS3Object", "fileName": "test.txt", "fileData": "aGVsbG8gd29ybGQK" }
            response = upload_file(self.event)
            assert response == 0, 'Service should upload file to s3'

    def test_delete_file(self):
        with patch.object(boto3, 'client', return_value=self.s3_client):
            self.event = {"operation": "delete_file", "fileName": "delete.txt"}
            response = delete_file(self.event)
            assert response == 0, 'Service should delete object from S3'