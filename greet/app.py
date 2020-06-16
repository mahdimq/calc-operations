from flask import Flask

app = Flask(__name__)


@app.route("/welcome")
def welcome_route():
    return f"<h1>WELCOME</h1>"


@app.route("/welcome/home")
def home_route():
    return f"<h1>WELCOME HOME</h1>"


@app.route("/welcome/back")
def back_route():
    return f"<h1>WELCOME BACK</h1>"
