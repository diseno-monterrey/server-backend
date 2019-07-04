#!/usr/bin/env python3

from flask import Flask, request
# import tinydb as db

app = Flask(__name__)


@app.route('/')
def index():
    return 'Server Setup'


@app.route('/hello')
def say_hello():
    return 'Hello from the world'


@app.route('/user/<username>')
def show_user(username):
    return f'Username is available: {username}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # returns the post, the post_id should be an int
    return str(post_id)
