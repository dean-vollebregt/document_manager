import unittest

from unittest.mock import MagicMock, Mock, patch, ANY

from lambdas.document_manager.lambda_handler import lambda_handler


class LambdaHandlerTestCase(unittest.TestCase):

    def setUp(self):
        self.mock_context = Mock()

    def testUploadFileInvoked(self):
        with patch('lambdas.document_manager.services.s3_service.upload_file') as upload_file_mock:
            self.mock_event = {"operation": "upload_file"}
            lambda_handler(self.mock_event, self.mock_context)
            upload_file_mock.assert_called_once(), 'The upload_file function is invoked'

    def testDeleteFileInvoked(self):
        with patch('lambdas.document_manager.services.s3_service.delete_file') as delete_file_mock:
            self.mock_event = {"operation": "delete_file"}
            lambda_handler(self.mock_event, self.mock_context)
            delete_file_mock.assert_called_once(), 'The upload_file function is invoked'

    def testStoreFileMetadataInvoked(self):
        with patch('lambdas.document_manager.services.dynamo_service.store_file_metadata') as store_file_metadata_mock:
            self.mock_event = {"operation": "store_file_metadata", "metadata": {"title": "test"}}
            lambda_handler(self.mock_event, self.mock_context)
            store_file_metadata_mock.assert_called_once(), 'The store_file_metadata function is invoked'

    def testReadFileMetadataInvoked(self):
        with patch('lambdas.document_manager.services.dynamo_service.read_file_metadata') as read_file_metadata_mock:
            self.mock_event = {"operation": "read_file_metadata"}
            lambda_handler(self.mock_event, self.mock_context)
            read_file_metadata_mock.assert_called_once(), 'The read_file_metadata function is invoked'

    def testDeleteFileMetadataInvoked(self):
        with patch('lambdas.document_manager.services.dynamo_service.delete_file_metadata') as delete_file_metadata_mock:
            self.mock_event = {"operation": "delete_file_metadata"}
            lambda_handler(self.mock_event, self.mock_context)
            delete_file_metadata_mock.assert_called_once(), 'The read_file_metadata function is invoked'