from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY']='eef0b0f58fd44c4d8d90fe6125477800'

from flaskblog import routes

