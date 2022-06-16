from flask import Flask
import rhino3dm as rhino

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'
