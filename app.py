from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello xddddddddd'

@app.route('hello 2/')
def azucar():
    return "I'm 20 years old"
