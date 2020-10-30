import unittest
from lambdas.document_manager.services.dynamo_service import store_file_metadata, read_file_metadata, delete_file_metadata


class TestDynamoService(unittest.TestCase):

    def test_store_file_metadata(self):
        event = { "operation": "store_file_metadata", "metadata": { "title": "test"}}
        response = store_file_metadata(event)
        self.assertEqual(response['ResponseMetadata']['HTTPStatusCode'], 200)

    def test_read_file_metadata(self):
        response = read_file_metadata()
        self.assertIn('fileName', response[0].keys())

    def test_delete_file_metadata(self):
        event = { "operation": "delete_file_metadata", "title": "test_entry" }
        response = delete_file_metadata(event)
        self.assertEqual(response['ResponseMetadata']['HTTPStatusCode'], 200)


if __name__ == '__main__':
    unittest.main()