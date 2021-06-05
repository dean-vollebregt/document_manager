import unittest
from lambdas.document_manager.services.s3_service import upload_file, delete_file


class TestS3Service(unittest.TestCase):

    def test_upload_file(self):
        event = { "operation": "createS3Object", "fileName": "test.txt", "fileData": "aGVsbG8gd29ybGQK" }
        response = upload_file(event)
        self.assertEqual(response['ResponseMetadata']['HTTPStatusCode'], 200)

    def test_delete_file(self):
        event = { "operation": "delete_file", "fileName": "delete.txt" }
        response = delete_file(event)
        self.assertEqual(response['ResponseMetadata']['HTTPStatusCode'], 204)


if __name__ == '__main__':
    unittest.main()