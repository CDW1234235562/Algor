from flask import Flask
import rhino3dm as rhino

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Link start!'


@app.route('/urlend')
def username():
    return {"username": 'Kirito'}
