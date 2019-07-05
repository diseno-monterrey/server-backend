#!/usr/bin/env python3

from flask import Flask, request, jsonify
from tinydb import TinyDB
from flask_cors import CORS

app = Flask(__name__)
db = TinyDB('db.json')
CORS(app)


@app.route('/')
def index():
    return 'Server Setup'


@app.route('/form-test', methods=['GET', 'POST'])
def get_database():
    return jsonify(db.all())


@app.route('/form-example', methods=['POST'])
# allow both GET and POST requests
def form_example():
    print(request.is_json)
    content = request.get_json()
    print(content)
    db.insert(content)
    return 'done'


@app.route('/user/<username>')
def show_user(username):
    return f'Username is available: {username}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # returns the post, the post_id should be an int
    return str(post_id)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
