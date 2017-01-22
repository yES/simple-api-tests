# -*- coding: utf-8 -*-

import json
from flask import Flask, request, make_response as response

import settings

app = Flask(__name__)


def get_data_by_id(book_id):
    if book_id == '1534622':
        return {
            'id': '1534622',
            'book_name': u'Война и мир',
            'book_author': u'Л.Н. Толстой',
            'creationDate': '1994-01-12',
        }

    return None


@app.route("/api/getBookById")
def get_book_by_id():
    book_id = request.args.get('id')
    data = get_data_by_id(book_id)

    content = {
        'response': {
            'code': 404,
            'data': {},
        }
    }
    if data:
        content['response']['code'] = 200
        content['response']['data'] = data

    resp = response(json.dumps(content), 200)
    resp.headers['Content-Type'] = 'application/json'

    return resp


if __name__ == "__main__":
    app.run(host=settings.HOST, port=settings.PORT)
