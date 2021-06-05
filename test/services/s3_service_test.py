import unittest

from unittest.mock import patch

from lambdas.document_manager.services.s3_service import upload_file, delete_file


class TestS3Services(unittest.TestCase):

    with patch('lambdas.document_manager.services.s3_service.boto3.client'):
        def test_upload_file(self):
            self.event = {"operation": "createS3Object", "fileName": "test.txt", "fileData": "aGVsbG8gd29ybGQK" }
            response = upload_file(self.event)
            assert response == None, 'Service should upload file to s3'

    with patch('lambdas.document_manager.services.s3_service.boto3.client'):
        def test_delete_file(self):
            self.event = {"operation": "delete_file", "fileName": "delete.txt"}
            response = delete_file(self.event)
            assert response == 0, 'Service should delete object from S3'