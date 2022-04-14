from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!!"

@app.route("/jefferson")
def hello_jefferson():
    return "Hello, Jefferson!!"

@app.route("/maria")
def hello_maria():
    return "Hello, Maria!!"