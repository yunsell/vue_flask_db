import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS
import dbModule
import json


BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': '점프 투 파이썬',
        'author': '파이씨',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'vue.js',
        'author': 'js씨',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': '마리아DB',
        'author': '마리씨',
        'read': True
    }
]

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def main():
    return jsonify('Hello World !')

@app.route('/test/', methods=['GET'])
def test():
    db_class = dbModule.Database()
    sql = "SELECT C.id contentId, C.title, \
                C.content_type contentType, C.clinic, C.clinic_div clinicDiv, \
                C.keyword, C.hospital, C.source, \
                U.user_name registerUserName, \
                C.created_at createdAt, C.updated_at updatedAt \
              FROM content C \
                LEFT JOIN user U \
                  ON C.register_user_id = U.id \
              WHERE C.deleted_at IS NULL \
              ORDER BY C.id DESC"
    row = db_class.executeAll(sql)
    return jsonify(row)

@app.route('/user/', methods=['GET'])
def ping_pong():
    db_class = dbModule.Database()
    sql = "SELECT id,email,password,user_name,profile_image,grade, \
        created_at,updated_at,deleted_at, IF(not_delete = 1, 1, 0) as del FROM user"
    row = db_class.executeAll(sql)
    return jsonify(row)

def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False

@app.route('/books/', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(debug=True)