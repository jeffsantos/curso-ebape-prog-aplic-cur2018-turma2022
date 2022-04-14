from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    subhead = "Greetings to the world"
    return render_template("index.html", subhead=subhead)

@app.route("/bye")
def bye():
    subhead = "Goodbye"
    return render_template("index.html", subhead=subhead)