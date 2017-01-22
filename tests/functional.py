# -*- coding: utf-8 -*-

import requests
import unittest

import settings


class TestBookById(unittest.TestCase):

    def setUp(self):
        testing_url = '{}/api/getBookById'.format(settings.BASE_URL)
        self.response = requests.get(testing_url, params={'id': '1534622'})
        self.json_response = self.response.json()

        self.data_id = '1534622'
        self.data_book_name = u'Война и мир'
        self.data_book_author = u'Л.Н. Толстой'
        self.data_creationDate = '1994-01-12'

    def test_api_response_code(self):
        self.assertEqual(self.json_response['response']['code'], 200)

    def test_data_id(self):
        self.assertEqual(self.json_response['response']['data']['id'], self.data_id)

    def test_data_book_name(self):
        self.assertEqual(self.json_response['response']['data']['book_name'], self.data_book_name)

    def test_data_book_author(self):
        self.assertEqual(self.json_response['response']['data']['book_author'], self.data_book_author)

    def test_data_creationDate(self):
        self.assertEqual(self.json_response['response']['data']['creationDate'], self.data_creationDate)


if __name__ == '__main__':
    unittest.main()
