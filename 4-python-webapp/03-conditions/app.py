import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    is_it_easter = (now.month == 4 and now.day == 4 and now.year == 2021)  

    return render_template("index.html", easter=is_it_easter)