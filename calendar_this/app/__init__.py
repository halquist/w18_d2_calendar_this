from flask import Flask
from app import routes
import os

app = Flask(__name__)
app.config.update({'SECRET_KEY': os.environ.get('SECRET_KEY')})
app.register_blueprint(routes.bp)
# app.register_blueprint(routes.daily)

# @app.route('/')
# def index():
#   return '<h1>App Here</h1>'
