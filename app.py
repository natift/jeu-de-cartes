from flask import Flask
from Zebi import lol

app = Flask(__name__)

@app.route("/")
def index():
    return lol()

