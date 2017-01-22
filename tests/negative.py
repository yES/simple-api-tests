# -*- coding: utf-8 -*-

import requests
import unittest

import settings


class TestNegativeCasesBookById(unittest.TestCase):

    def setUp(self):
        self.testing_url = '{}/api/getBookById'.format(settings.BASE_URL)

    def test_api_response_with_empty_id(self):
        response = requests.get(self.testing_url, params={'id': ''})
        json_response = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response['response']['code'], 404)

    def test_api_response_with_incorrect_id(self):
        response = requests.get(self.testing_url, params={'id': 'incorrect'})
        json_response = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response['response']['code'], 404)

if __name__ == '__main__':
    unittest.main()
