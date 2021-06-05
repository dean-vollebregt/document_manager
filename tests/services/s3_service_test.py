import unittest

from unittest import mock
from lambdas.document_manager.services.s3_service import upload_file, delete_file


class TestS3Services(unittest.TestCase):

    def setUp(self):
        self.s3_mock = mock

    @mock.patch('lambdas.document_manager.services.s3_service.boto3.client')
    def test_upload_file(self, s3_mock):
        self.event = {"operation": "createS3Object", "fileName": "test.txt", "fileData": "aGVsbG8gd29ybGQK" }
        response = upload_file(self.event)
        assert response == None, 'Service should upload file to s3'

    @mock.patch('lambdas.document_manager.services.s3_service.boto3.client')
    def test_delete_file(self, s3_mock):
        self.event = {"operation": "delete_file", "fileName": "delete.txt"}
        response = delete_file(self.event)
        assert response == 0, 'Service should delete object from S3'