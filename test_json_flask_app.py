"""Unit tests for the JSON Flask app wrapper."""

import httplib
import json
import unittest

import rookeries


class JsonFlaskAppUnitTestCase(unittest.TestCase):

    def setUp(self):
            self.test_app = rookeries.app.test_client()

    def test_make_json_error_creates_a_404_missing_page_error_json(self):
        test_path = '/some/non-existent/path'
        expected_error = {
            'error': {
                'code': httplib.NOT_FOUND,
                'message': 'Not Found',
            }
        }

        actual = self.test_app.get(test_path)
        self.assertIsNotNone(actual)
        self.assertEqual(actual.status_code, httplib.NOT_FOUND)
        actual_json = json.loads(actual.data)
        self.assertDictEqual(actual_json, expected_error
