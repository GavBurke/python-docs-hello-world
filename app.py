from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, from gavinburke.azurewebsites.net</p>"

@app.route("/test")
def test():
    return "<p>Hello from /test page!</p>"
