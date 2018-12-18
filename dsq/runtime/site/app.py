from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "index page."

@app.route('/preprocessing')
def preprocessing():
    return "preprocessing page."

@app.route('/predicting')
def predicting():
    return "predicting page."

@app.route('/ensembling')
def ensenmbling():
    return "ensembling page."