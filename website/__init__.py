from flask import Flask

# Initialize flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dnd prototype'

    return app
    