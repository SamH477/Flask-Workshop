from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='../templates')

@app.route("/")
def home():
    pass

@app.route("/greet", methods=["POST"])
def greet():
    pass

@app.route("/welcome")
def welcome():
    pass

if __name__ == "__main__":
    app.run(debug=True)