# -*- coding: utf-8 -*-
import datetime
import requests
import unittest

import settings


class TestApiAnswerFormat(unittest.TestCase):

    @staticmethod
    def is_string_to_datetime_convertable(string_date):
        try:
            datetime.datetime.strptime(string_date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def setUp(self):
        testing_url = '{}/api/getBookById'.format(settings.BASE_URL)
        self.response = requests.get(testing_url, params={'id': '1534622'})
        self.json_response = self.response.json()

    def test_api_field_response_exists(self):
        self.assertTrue('response' in self.json_response, 'API response has not field "response"')

    def test_api_field_response_type(self):
        self.assertTrue(
            isinstance(self.json_response['response'], dict),
            'API response field "response" must be JSON object'
        )

    def test_api_field_response_code_exists(self):
        self.assertTrue('code' in self.json_response['response'], 'API response has not field "response.code"')

    def test_api_field_response_code_type(self):
        self.assertTrue(
            isinstance(self.json_response['response']['code'], int),
            'API response field "response.code" must has int type'
        )

    def test_api_field_response_data_exists(self):
        self.assertTrue('data' in self.json_response['response'], 'API response has not field "response.data"')

    def test_api_field_response_data_type(self):
        self.assertTrue(
            isinstance(self.json_response['response']['data'], dict),
            'API response field "response.data" must be JSON object'
        )

    def test_api_field_response_data_id_exists(self):
        self.assertTrue('id' in self.json_response['response']['data'], 'API response has not field "response.data.id"')

    def test_api_field_response_data_id_type(self):
        self.assertTrue(
            isinstance(self.json_response['response']['data']['id'], unicode),
            'API response field "response.data.id" must has string type'
        )

    def test_api_field_response_data_book_name_exists(self):
        self.assertTrue(
            'book_name' in self.json_response['response']['data'],
            'API response has not field "response.data.book_name"'
        )

    def test_api_field_response_data_book_name_type(self):
        self.assertTrue(
            isinstance(self.json_response['response']['data']['book_name'], unicode),
            'API response field "response.data.book_name" must has string type'
        )

    def test_api_field_response_data_book_author_exists(self):
        self.assertTrue(
            'book_author' in self.json_response['response']['data'],
            'API response has not field "response.data.book_author"'
        )

    def test_api_field_response_data_book_author_type(self):
        self.assertTrue(
            isinstance(self.json_response['response']['data']['book_author'], unicode),
            'API response field "response.data.book_author" must has string type'
        )

    def test_api_field_response_data_creationDate_exists(self):
        self.assertTrue(
            'creationDate' in self.json_response['response']['data'],
            'API response has not field "response.data.creationDate"'
        )

    def test_api_field_response_data_creationDate_type(self):
        self.assertTrue(
            isinstance(self.json_response['response']['data']['creationDate'], unicode),
            'API response field "response.data.creationDate" must has string type'
        )

    def test_api_field_response_data_creationDate_format(self):
        self.assertTrue(
            self.is_string_to_datetime_convertable(self.json_response['response']['data']['creationDate']),
            'API response field "response.data.creationDate" must has format "%Y-%m-%d"'
        )

if __name__ == '__main__':
    unittest.main()
