# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Hello, this is PetFax!"

# @app.route('/pets')
# def pets():
#     return "These are our pets!"

from petfax import create_app
app = create_app()